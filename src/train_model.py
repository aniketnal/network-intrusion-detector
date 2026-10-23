import os
import pandas as pd
import numpy as np
import joblib
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

def run_pipeline():
    data_path = "data/network_traffic.csv"
    if not os.path.exists(data_path):
        print("Data file not found. Generating sample data...")
        from generate_data import generate_synthetic_network_data
        generate_synthetic_network_data(data_path)
        
    print("Loading network traffic dataset...")
    df = pd.read_csv(data_path)
    
    df['target'] = df['label'].apply(lambda x: 'normal' if x == 'normal' else 'anomaly')
    X = df.drop(columns=['label', 'target'])
    y = df['target']
    
    categorical_cols = ['protocol_type', 'service', 'flag']
    encoders = {}
    
    for col in categorical_cols:
        le = LabelEncoder()
        X[col] = le.fit_transform(X[col])
        encoders[col] = le
        
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )
    
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    
    print("Training Random Forest Classifier...")
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train_scaled, y_train)
    
    y_pred = model.predict(X_test_scaled)
    acc = accuracy_score(y_test, y_pred)
    
    print("=" * 50)
    print(f"Model Accuracy: {acc * 100:.2f}%")
    print("=" * 50)
    print("Classification Report:\n")
    print(classification_report(y_test, y_pred))
    
    os.makedirs("models", exist_ok=True)
    joblib.dump(model, "models/nids_model.pkl")
    joblib.dump(scaler, "models/scaler.pkl")
    joblib.dump(encoders, "models/encoders.pkl")
    print("Saved model and preprocessing artifacts to 'models/' directory.")

if __name__ == "__main__":
    run_pipeline()
