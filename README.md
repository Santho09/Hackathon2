

# **🚀 AI-Powered Healthcare Recommender System**  

## **📌 Overview**  
The **AI-Powered Healthcare Recommender System** provides **personalized health insights** based on **diet, workout, sleep, and medicine recommendations**. The system analyzes user inputs (e.g., age, weight, height, activity level, sleep patterns, diseases) and **leverages Machine Learning (ML) models** to generate tailored recommendations.  

### **✨ Key Features:**  
✅ AI-Powered **Diet Recommendations**  
✅ **Personalized Workout Plans**  
✅ **Sleep Health Insights** & Recommendations  
✅ **Medicine Recommender** Based on Health Conditions  
✅ **Interactive Dashboard & Intuitive UI**  

---

## **📁 Code Structure**  

### **🔹 Backend (Node.js & Express)**
📂 **backend/**  
- 📂 **routes/** → API routes (`diet.js`, `workout.js`, `sleep.js`, `medicine.js`)  
- 📂 **models/** → MongoDB schemas  
- 📂 **utils/** → Utility functions  
- 📜 **server.js** → Main Express server setup  

### **🔹 Frontend (React.js & TailwindCSS)**
📂 **client/**  
- 📂 **src/**  
  - 📂 **components/** → UI components  
  - 📂 **pages/** → Individual pages for diet, workout, etc.  
  - 📜 **App.js** → Main React component  

### **🔹 Machine Learning (Python & Flask)**
📂 **ml/**  
- 📜 `diet_ml.py` → ML model for diet recommendations  
- 📜 `workout_ml.py` → ML model for workout recommendations  
- 📜 `sleep_ml.py` → ML model for sleep recommendations  
- 📜 `medicine_ml.py` → ML model for medicine recommendations  

📂 **flask_apis/**  
- 📜 `diet_api.py` → Flask API for diet recommendations  
- 📜 `workout_api.py` → Flask API for workout recommendations  
- 📜 `sleep_api.py` → Flask API for sleep recommendations  
- 📜 `medicine_api.py` → Flask API for medicine recommendations  

---

## **📦 Dependencies**  

### **🔹 Backend (Node.js & Express)**
- `express` → Web framework  
- `mongoose` → MongoDB ODM  
- `axios` → API communication  
- `cors` → Cross-origin requests  
- `dotenv` → Environment variable management  

### **🔹 Frontend (React.js)**
- `react` → UI framework  
- `axios` → API requests  
- `react-router-dom` → Page navigation  
- `tailwindcss` → Styling  

### **🔹 Machine Learning (Python & Flask)**
- `flask` → API framework  
- `scikit-learn` → ML models  
- `pandas` & `numpy` → Data processing  
- `joblib` → Model serialization  

---

## **🚀 Setup & Execution**  

### **1️⃣ Prerequisites**  
✅ **Node.js** installed  
✅ **Python 3.8+** installed  
✅ **MongoDB** installed or use **MongoDB Atlas**  

---

### **2️⃣ Backend Setup (Node.js & Express)**  

1️⃣ Navigate to the backend folder  
```bash
cd backend1
```
2️⃣ Install dependencies  
```bash
npm install
```
3️⃣ Start the server  
```bash
npm start
```
✅ **Runs on:** `http://localhost:5000`

---

### **3️⃣ Frontend Setup (React.js)**  

1️⃣ Navigate to the frontend folder  
```bash
cd client1
```
2️⃣ Install dependencies  
```bash
npm install
```
3️⃣ Start React app  
```bash
npm start
```
✅ **Runs on:** `http://localhost:3000`

---

### **4️⃣ ML API Setup (Flask)**  

1️⃣ Navigate to the `ml` folder  
```bash
cd ml
```
2️⃣ Create a virtual environment  
```bash
python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate  # Windows
```
3️⃣ Install dependencies  
```bash
pip install -r requirements.txt
```
4️⃣ Start Flask APIs  
```bash
python diet_api.py       # Runs on http://127.0.0.1:5001
python workout_api.py    # Runs on http://127.0.0.1:5003
python sleep_api.py      # Runs on http://127.0.0.1:5005
python medicine_api.py   # Runs on http://127.0.0.1:5004
```

---

## **✅ Expected Output**  

- **Users input their health details** (Age, Weight, Activity, Sleep, Disease, etc.).  
- **AI analyzes data** & provides personalized recommendations for:
  - **Diet** (custom meal plans & recipes)
  - **Workout** (weekly exercise schedules)
  - **Sleep** (health insights & improvement tips)
  - **Medicine** (suggestions based on condition)  

---

## **📌 Additional Considerations**  

### **🔹 Git Commit Guidelines**
- **Meaningful commit messages** (e.g., `Added diet recommendation API`).  
- **Separate branches** for new features (`feature/diet-recommender`).  
- **Merge changes via Pull Requests (PRs)** for code review.  

### **🔹 Deployment (Optional)**
- **Frontend:** Vercel / Netlify  
- **Backend & Flask APIs:** Render / AWS EC2 / DigitalOcean  
- **Database:** MongoDB Atlas  

---

## **🎯 Conclusion**  

This **AI-powered Health Recommender System** integrates **Machine Learning & Data Science** to provide **personalized health insights** for users. The combination of **Flask ML models, Express backend, and React frontend** ensures a **scalable, intuitive, and secure** platform for promoting **better health habits**.  

🚀 **Ready to make health smarter with AI!** 💡  
