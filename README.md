# BMI Calculator (Flask + React)

A simple and interactive **BMI Calculator** built with **Flask (backend)** and React **(frontend)**.
Users can enter their height and weight in different units, and the app calculates and categorizes the BMI.

## 🚀 Features

<ul><li>Supports height input in <b>feet/inches</b> or <b>centimeters</b>.</li></ul>
<ul><li>Supports weight input in <b>pounds</b> or <b>kilograms</b>.</li></ul>
<ul><li>Calculates BMI and displays <b>weight category (Underweight, Normal, Overweight, Obese)</b>.</li></ul>
<ul><li>Interactive and dynamic UI built with React.</li></ul>
<ul><li>API-based calculation using Flask for backend processing.</li></ul>

## 🛠️ Technologies Used

<ul><li><b>Frontend:</b> React, JavaScript, CSS</li></ul>
<ul><li><b>Backend:</b> Flask (Python)</li></ul>
<ul><li><b>Communication:</b> Fetch API (JSON requests)</li></ul>

## 📂 Project Structure

```
BMI_Calculator/
│── backend/               # Flask Backend
│   ├── app.py             # Main Flask App
│   ├── static/            # CSS, JS, Images (if needed)
│   ├── templates/         # HTML Templates
│   ├── requirements.txt   # Python dependencies
│── bmi-react/             # React Frontend
│   ├── src/               # React Components
│   ├── public/            # Static Assets
│   ├── package.json       # React dependencies
│   ├── .gitignore         # Ignore node_modules
│── README.md              # Project Documentation
│── .gitignore             # Global ignore rules
```

## 🏗️ Installation & Setup
### 1️⃣ Clone the Repository
```
git clone https://github.com/your-username/BMI-calculator.git
cd BMI-calculator
```
### 2️⃣ Setup & Run the Backend (Flask)
```
cd backend
python3 -m venv venv  # Create virtual environment
source venv/bin/activate  # Activate venv (Windows: venv\Scripts\activate)
pip install -r requirements.txt  # Install dependencies
python app.py  # Start Flask server
```
🚀 Flask API will run on: ```http://127.0.0.1:5000```
### 3️⃣ Setup & Run the Frontend (React)
```
cd bmi-react
npm install  # Install dependencies
npm start  # Start React app
```
🚀 React app will run on: http://localhost:3000

## 🎯 Usage
1. Enter **height** in either ```feet & inches``` or ```centimeters```.
2. Enter **weight** in either ```pounds``` or ```kilograms```.
3. Click **"Calculate BMI"**.
4. View **BMI result & weight category**.

## 🔧 Deployment
### 🛠 Deploying React inside Flask
1. **Build React** for production:
   ```
   cd bmi-react
   npm run build
   ```
2. **Move the ```build/``` folder inside ```backend/```:**
   ```
   mv build ../backend/
   ```
3. **Modify ```backend/app.py``` to serve React:**
   ```
   from flask import Flask, send_from_directory

   app = Flask(__name__, static_folder="build", static_url_path="/")

   @app.route("/")
   def serve_react():
       return send_from_directory(app.static_folder, "index.html")

   if __name__ == "__main__":
       app.run(debug=True)
   ```
4. **Run Flask again:**
   ```
   cd backend
   python app.py
   ```
🚀 Now, your React app will be served by Flask at ```http://127.0.0.1:5000```.

## 🤝 Contributing
1. **Fork** the repository.
2. **Create** your feature branch (```git checkout -b feature-name```).
3. **Commit** your changes (```git commit -m "Added feature"```).
4. **Push** to the branch (```git push origin feature-name```).
5. **Open a Pull Request.**


## 📜 License
This project is open-source and available under the MIT License.


