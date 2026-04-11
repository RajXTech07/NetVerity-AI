# 🏗️ NetVerity AI — System Architecture

## 📌 Overview

NetVerity AI is a full-stack web application that analyzes WiFi reliability using AI-based predictions and presents results through an interactive speed test UI.

---

## 🧠 High-Level Architecture

```
Frontend (Speed Test Meter)
        ↓
API Layer (FastAPI Backend)
        ↓
Business Logic Layer
        ↓
AI Model (Decision Tree)
        ↓
Database (Optional)
```

---

## ⚙️ Components Breakdown

### 1️⃣ Frontend Layer

**Tech:** HTML-CSS-JS

Responsible for:

* Speed test UI (Ookla-style simulation)
* Collecting network parameters
* Sending API requests
* Displaying:

  * Trust Score
  * Status
  * Recommendations

---

### 2️⃣ API Layer (FastAPI)

Handles:

* Incoming requests (`/recommend`)
* Data validation (Pydantic models)
* Routing to services

---

### 3️⃣ Business Logic Layer

Located in:

```
backend/app/services/
```

Responsibilities:

* Data preprocessing
* Calling AI model
* Generating recommendations
* Applying rules (if needed)

---

### 4️⃣ AI Model Layer

**Model:** Decision Tree Classifier

Located in:

```
ai-model/model.pkl
```

Used for:

* Predicting WiFi quality score
* Classifying network performance

---

### 5️⃣ Database Layer (Optional)

Used for:

* Storing user test results
* Tracking history
* Future analytics

---

## 🔄 Data Flow

```
User clicks "Start Test"
        ↓
Frontend simulates speed test
        ↓
Collected data sent to backend
        ↓
Backend preprocesses data
        ↓
AI model predicts result
        ↓
Response sent back to frontend
        ↓
UI displays score + recommendation
```

---

## 📊 Input Features

* Download speed
* Upload speed
* Ping
* Jitter
* Packet loss
* Signal strength
* Users connected
* Time of day
* Location type

---

## 🎯 Output

* Trust Score (0–100)
* Status (Excellent / Good / Moderate / Poor)
* Recommendation

---

## 🔐 Scalability Considerations

* Replace simulated speed test with real measurement
* Use cloud-based backend (AWS/GCP)
* Add database (PostgreSQL/MongoDB)
* Train model on real user data

---

## 🚀 Future Architecture Upgrade

```
Frontend
   ↓
API Gateway
   ↓
Microservices
   ↓
ML Model Server
   ↓
Cloud Database
```

---

## 🏆 Key Strengths

* AI-driven decision making
* Clean modular architecture
* Scalable design
* Real-world applicability

---

🔥 *Designed for scalability and real-world deployment*
