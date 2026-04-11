from pathlib import Path

import joblib
import pandas as pd

# =================================
# Load the pre-trained model
# =================================

# .parents[2] points to the 'backend' folder
BASE_DIR = Path(__file__).resolve().parents[2] 
MODEL_DIR = BASE_DIR / "ai-model"

# Load the files from the new location
model = joblib.load(MODEL_DIR / "model.pkl")
columns = joblib.load(MODEL_DIR / "columns.pkl")

# =================================
# same columns as training data
# =================================

MODEL_COLUMNS = columns

def preprocess_input(data):
    
    # keep original input data intact and normalize categorical values
    data = data.copy()
    if 'times_of_day' in data:
        data['time_of_day'] = str(data.pop('times_of_day')).strip().lower()
    if 'time_of_day' in data:
        data['time_of_day'] = str(data['time_of_day']).strip().lower()
    if 'location_type' in data:
        data['location_type'] = str(data['location_type']).strip().lower()

    df = pd.DataFrame([data])

    # converts categorical to numeric using the training column naming scheme
    df = pd.get_dummies(df, columns=['time_of_day', 'location_type'])

    # Add missing columns
    for col in MODEL_COLUMNS:
        if col not in df:
            df[col] = 0

    # Ensure the order matches the training data
    df = df[MODEL_COLUMNS]
    return df

# =================================
# Predict the data
# =================================

def predict(data):
    preprocessed = preprocess_input(data)
    
    # Get the base score from your AI model (Assuming it returns a value 0-5)
    prediction = model.predict(preprocessed)[0]
    ai_base_score = prediction * 20 # Convert to 0-100 scale
    
    # Optional: Combine AI score with real-time metrics for a 'Trust Score'
    # We will give 60% weight to AI prediction and 40% to current hardware metrics
    manual_metrics = int((
        data["download"] * 0.4 + 
        data["upload"] * 0.2 + 
        (100 - data["ping"]) * 0.2 + 
        (100 - data["jitter"]) * 0.1 + 
        (100 - data["packet_loss"] * 10) * 0.1
    ))
    
    # Final AI-Weighted Trust Score
    trust_score = int((ai_base_score * 0.6) + (manual_metrics * 0.4))
    
    # Ensure score stays within 0-100
    trust_score = max(0, min(100, trust_score))

    # Network Status Logic
    if trust_score >= 80:
        status = "Excellent Network Speed"
    elif trust_score >= 50:
        status = "Good Network Speed"
    elif trust_score >= 20:
        status = "Fair Network Speed"
    else:
        status = "Worst Network Speed"
        
    return trust_score, status
 