import joblib
import pandas as pd
import numpy as np

def predict_sample():
    print("Loading model and artifacts...")
    model = joblib.load("models/nids_model.pkl")
    scaler = joblib.load("models/scaler.pkl")
    encoders = joblib.load("models/encoders.pkl")
    
    sample_data = {
        'duration': [0.0],
        'protocol_type': ['tcp'],
        'service': ['http'],
        'flag': ['S0'],
        'src_bytes': [0],
        'dst_bytes': [0],
        'wrong_fragment': [0],
        'urgent': [0],
        'hot': [0],
        'num_failed_logins': [0],
        'count': [250],
        'srv_count': [250],
        'serror_rate': [0.98],
        'rerror_rate': [0.0]
    }
    
    df_sample = pd.DataFrame(sample_data)
    
    for col, le in encoders.items():
        df_sample[col] = le.transform(df_sample[col])
        
    sample_scaled = scaler.transform(df_sample)
    
    prediction = model.predict(sample_scaled)[0]
    probabilities = model.predict_proba(sample_scaled)[0]
    classes = model.classes_
    
    print("\n--- Prediction Result ---")
    print(f"Classified Traffic Status: {prediction.upper()}")
    for cls, prob in zip(classes, probabilities):
        print(f"Confidence ({cls}): {prob*100:.2f}%")

if __name__ == "__main__":
    predict_sample()
