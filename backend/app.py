from flask import Flask, request, jsonify
from flask_cors import CORS  # Enable cross-origin requests

app = Flask(__name__, static_folder="bmi-react/build", static_url_path="/")
CORS(app)  # Allow frontend requests (useful if frontend runs on a different port)

@app.route("/")
def index():
    return app.send_static_file("index.html")

@app.route("/calculate", methods=["POST"])
def calculate():
    try:
        data = request.get_json()

        # Extract values, defaulting to 0 if missing
        feet = float(data.get("feet", 0))
        inches = float(data.get("inches", 0))
        cm = float(data.get("cm", 0))
        pounds = float(data.get("pounds", 0))
        kg = float(data.get("kg", 0))

        # Convert height to cm if given in feet/inches
        if cm == 0 and feet > 0:
            total_inches = (feet * 12) + inches
            cm = total_inches * 2.54  # Convert inches to cm

        # Convert weight to kg if given in pounds
        if kg == 0 and pounds > 0:
            kg = pounds * 0.453592  # Convert lbs to kg

        # Ensure valid height & weight
        if cm <= 0 or kg <= 0:
            return jsonify({"error": "Height and weight must be positive values."}), 400

        # Convert height to meters
        height_m = cm / 100
        bmi = round(kg / (height_m ** 2), 2)

        # Determine BMI category
        category = (
            "Underweight" if bmi < 18.5 else
            "Normal weight" if bmi < 24.9 else
            "Overweight" if bmi < 29.9 else
            "Obese"
        )

        return jsonify({"bmi": bmi, "category": category})

    except (ValueError, TypeError):
        return jsonify({"error": "Invalid input. Please provide numeric values."}), 400

# Serve React static files
@app.route("/<path:path>")
def static_proxy(path):
    return app.send_static_file(path)

if __name__ == "__main__":
    app.run(debug=True)
