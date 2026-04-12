# 🚀 NetVerity AI — WiFi Trust Analyzer

> **AI-powered WiFi reliability checker for remote workers, students, and travelers**
> 
> **Must refresh the app 2 to 3 times to run perfectly**

---

## 🌍 Problem Statement

In today’s remote-first world, people depend heavily on internet connectivity.
Hotels, cafés, and coworking spaces often claim **“high-speed WiFi”**, but in reality:

* Speeds are inconsistent
* Connections drop during meetings
* No way to verify reliability beforehand

👉 Users lack a **trustable system to evaluate WiFi quality in real-time**

---

## 💡 Solution

**NetVerity AI** provides:

* A **Speed Test Interface** (modern UI like real tools)
* AI-based **WiFi Trust Score (0–100)**
* Smart **recommendations based on network conditions**
* Future-ready architecture for **real network testing**

---

## 🎯 Key Features

### ⚡ Speed Test Interface

* Circular animated speed meter
* Real-time testing phases:

  * Download test
  * Upload test
  * Ping analysis

---

### 🤖 AI-Based Trust Scoring

* Uses Machine Learning (Decision Tree)
* Predicts network quality:

  * Excellent 🚀
  * Good 👍
  * Moderate ⚠️
  * Poor ❌

---

### 📊 Smart Recommendations

* Suggests:

  * Best time for meetings
  * Suitable work type
* Example:

  * “Good for meetings in morning”
  * “Avoid video calls at night”

---

### 🧠 Intelligent Inputs

* Download speed
* Upload speed
* Ping (latency)
* Jitter
* Packet loss
* Signal strength
* Users connected
* Time of day
* Location type

---

## 🏗️ Project Architecture

```
Frontend (UI)
        ↓
Speed Test UI
        ↓
FastAPI Backend
        ↓
AI Model (Decision Tree)
        ↓
Trust Score + Recommendation
        ↓
(Optional) Database
```

---

## 📁 Project Structure

```
netverity-ai/
│
├── frontend/
│   ├── index.html          # Main page
│   ├── test.html           # Run WiFi test
│   ├── result.html         # Show results
│   ├── map.html            # Show nearby places --- For Future Enhancements
│   │
│   ├── css/
│   │   └── styles.css
│   │
│   ├── js/
│      ├── app.js          # General logic
│      ├── api.js          # API calls
│      ├── wifi.js         # Speed test + score
│      └── map.js          # Map logic---- For Future Enhancements
│   
│   
│
├── backend/                 # FastAPI Server
│   ├── app/
│   │   ├── main.py          # Entry point
│   │   │
│   │   ├── routes/          # API routes
│   │   │   ├── wifi.py
│   │   │   └── recommendation.py
│   │   │
│   │   ├── models/          # Data models
│   │   │   └── wifi_model.py
│   │   │
│   │   ├── services/        # Business logic
│   │   │   ├── wifi_service.py
│   │   │   └── ai_service.py
│   │   │
│   │   ├── db/              # Database connection
│   │   │   └── database.py
│   │   │
│   │   └── utils/
│   │       └── score_calculator.py
│   │
│   ├── ai-model/                # ML Model (Optional for hackathon)
│   │      ├── train.py
│   │      ├── model.pkl
│   │      ├── columns.pkl
│   │      └── dataset.csv
│   ├── requirements.txt
│   └── run.py
│
│
│
├── docs/                   # Documentation
│   ├── architecture.md
│   └── api-docs.md
│
├── .env                    # Environment variables
├── README.md
└── .gitignore
```

---

## ⚙️ Tech Stack

### Frontend

* HTML, CSS
* JavaScript

### Backend

* FastAPI
* Python

### AI / ML

* Scikit-learn
* Decision Tree Classifier

### Database (Optional)

* SQLite

---

## 🚀 How It Works

1. User clicks **Start Test**
2. UI simulates speed testing
3. Network parameters are collected
4. Data sent to backend API
5. AI model predicts:

   * Trust Score
   * Status
   * Recommendation
6. Results displayed to user

---

## 📡 API Endpoint

### POST `/recommend`

#### Request:

```json
{
  "download": 65,
  "upload": 12,
  "ping": 20,
  "jitter": 5,
  "users_connected": 20,
  "signal_strength": -60,
  "packet_loss": 1,
  "time_of_day": "afternoon",
  "location_type": "hotel"
}
```

---

#### Response:

```json
{
  "trust_score": 78,
  "status": "Good 👍",
  "recommendation": "Good for normal work"
}
```

---

## 🛠️ Installation & Setup

### 1️⃣ Clone Repository

```
git clone https://github.com/your-username/netverity-ai.git
cd netverity-ai
```

---

### 2️⃣ Backend Setup

```
cd backend
pip install -r requirements.txt
uvicorn app.main:app --reload
```

---

### 3️⃣ Frontend Setup

```
cd frontend
npm install
npm run dev
```

---

### 4️⃣ Train AI Model

```
cd ai-model
python train.py
```

---

## 🔮 Future Enhancements

* Real-time speed test (actual network measurement)
* WiFi ranking by location
* User history dashboard
* Map view wife (shows best cafe, Best speed wifi Hotels).
* search bar where --- "Best hotels in kolkata with high speed WIFI" and It shows suggestions.
* Mobile app version
* Cloud deployment

---

## 🏆 Hackathon Value

* Real-world problem solving
* AI + Web integration
* Clean architecture
* Strong UI/UX
* Scalable product idea

---

## 💬 Pitch Line

> “NetVerity AI helps users verify WiFi reliability instantly using AI-powered trust scoring and smart recommendations.”

---

## 👨‍💻 Author

**Raj Kumar**
Aspiring Ai-Engineer | AI & ML Enthusiast

---

## 📜 License

This project is for educational and hackathon purposes.

---

## ⭐ Final Note

> Speed test is currently simulated due to browser limitations.
> AI model and scoring logic are fully functional and ready for real-world integration.

---

🔥 *Built for impact. Designed for innovation.*
