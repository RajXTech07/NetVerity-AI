import pandas as pd
import joblib
import os

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score,classification_report

# =================================
# Load the dataset
# =================================

def load_data():
    data = pd.read_csv('ai-model/dataset.csv')
    print("Dataset loaded successfully.")
    return data

# =================================
# Prepeocess the data
# =================================

def preprocess_data(data):
    print("Preprocessing data...")
    
# Convert columns to numeric.
    data = pd.get_dummies(data, columns = ["time_of_day", "location_type"])
    return data

# =================================
# Split data
# =================================

def split_data(data):
    X = data.drop("quality", axis = 1)
    y = data["quality"]
    
    return train_test_split(X, y, test_size=0.2, random_state=42)

# =================================
# Train Model
# =================================

def train_model(X_train, y_train):
    print("Training model...")
    
    model = DecisionTreeClassifier()
    model.fit(X_train, y_train)
    return model

# =================================
# Evaluate Model
# =================================

def evaluate_model(model, X_test, y_test):
    print("Evaluating model...")
    
    y_pred = model.predict(X_test)
    
    print("\nAccuracy:", accuracy_score(y_test, y_pred))
    print("\nClassification Report:\n")
    print(classification_report(y_test, y_pred))

# =================================
# Save Model
# =================================

def save_model(model, X_train):
    print("Saving model...")
    
    joblib.dump(model, "ai-model/model.pkl")
    print("Model.pkl saved successfully.")
    
    joblib.dump(X_train.columns.tolist(), "ai-model/columns.pkl")
    print("Columns.pkl saved successfully.")
    
# =================================
# Main pipeline
# =================================

def main():
    data = load_data()
    data = preprocess_data(data)
    
    X_train, X_test, y_train, y_test = split_data(data)
    model = train_model(X_train, y_train)
    evaluate_model(model, X_test, y_test)
    save_model(model, X_train)
    
# =================================
# Entry Point
# =================================

if __name__ == "__main__":
    main()