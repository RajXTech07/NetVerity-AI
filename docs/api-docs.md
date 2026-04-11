# 📡 NetVerity AI — API Documentation

## 📌 Base URL

```
http://127.0.0.1:8000
```

---

## 🚀 Endpoint: WiFi Recommendation

### 🔹 POST `/recommend`

Predicts WiFi trust score and provides recommendations.

---

## 📥 Request Body

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

## 📌 Field Description

| Field           | Type   | Description                   |
| --------------- | ------ | ----------------------------- |
| download        | int    | Download speed (Mbps)         |
| upload          | int    | Upload speed (Mbps)           |
| ping            | int    | Latency (ms)                  |
| jitter          | int    | Network fluctuation           |
| users_connected | int    | Number of users on network    |
| signal_strength | int    | WiFi signal strength (dBm)    |
| packet_loss     | int    | Packet loss percentage        |
| time_of_day     | string | morning / afternoon / evening |
| location_type   | string | hotel / cafe / office         |

---

## 📤 Response

```json
{
  "trust_score": 78,
  "status": "Good 👍",
  "recommendation": "Good for normal work"
}
```

---

## 📊 Response Fields

| Field          | Description                    |
| -------------- | ------------------------------ |
| trust_score    | WiFi reliability score (0–100) |
| status         | Network quality category       |
| recommendation | Suggested usage                |

---

## ❌ Error Responses

### 422 Unprocessable Entity

Occurs when:

* Missing fields
* Wrong data types

---

## 🧪 Example cURL Request

```bash
curl -X POST "http://127.0.0.1:8000/recommend" \
-H "Content-Type: application/json" \
-d '{
  "download": 70,
  "upload": 15,
  "ping": 25,
  "jitter": 4,
  "users_connected": 10,
  "signal_strength": -50,
  "packet_loss": 0,
  "time_of_day": "morning",
  "location_type": "office"
}'
```

---

## 🔧 Testing

Use:

* Browser: `/docs` (Swagger UI)
* Postman
* cURL

---

## 🔐 CORS Note

If frontend cannot connect:

Enable CORS in FastAPI:

```python
from fastapi.middleware.cors import CORSMiddleware
```

---

## 🚀 Future APIs

* `/history` → Get past tests
* `/locations` → WiFi ranking
* `/predict-time` → Best time to use WiFi

---

🔥 *Simple, scalable, and ready for integration*
