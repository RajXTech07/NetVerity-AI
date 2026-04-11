from pathlib import Path

import joblib
import pandas as pd

# =================================
# Load the pre-trained model
# =================================

BASE_DIR = Path(__file__).resolve().parents[3]
MODEL_DIR = BASE_DIR / "ai-model"
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
    prediction = model.predict(preprocessed)[0]
    
    # Convert to the trust score(0-100)
    trust_score = prediction * 20
    trust_score = int((
        data["download"]*0.4 +
        data["upload"]*0.2 +
        (100-data["ping"]) * 0.2 +
        (100-data["jitter"]) * 0.1 +
        (100-data["packet_loss"]*10) * 0.1 ))
    
    #Network-Status
    if trust_score >= 80:
        status = "Excellent Network Speed"
        
    if trust_score >= 50:
        status = "Good Network Speed"
        
    #if trust_score >= 20:
        #status = "Fair Network Speed"
        
    else:
        status = "Worst Network Speed"
        
    return trust_score, status
    
 