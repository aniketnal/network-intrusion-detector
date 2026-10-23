# ML Network Intrusion Detector 🛡️💻

A machine learning solution built using Python and Scikit-learn to classify network traffic anomalies and detect potential cyber attacks.

---

## 📁 Repository Structure

```text
ml_network_intrusion_detector/
├── data/
│   └── network_traffic.csv     # Synthetic network traffic dataset
├── models/
│   ├── nids_model.pkl          # Trained Random Forest model
│   ├── scaler.pkl              # Scaler transformation object
│   └── encoders.pkl            # Categorical feature encoders
├── src/
│   ├── generate_data.py        # Generates network dataset
│   ├── train_model.py          # Data processing and training pipeline
│   └── predict.py              # Real-time inference script
├── requirements.txt            # Python dependencies
├── PROJECT_REPORT.md           # Complete academic project report
└── README.md                   # Setup and usage guide
```

---

## ⚙️ Setup and Installation Instructions

### Prerequisites
- Python 3.8 or higher installed on your system.

### Step 1: Open Terminal / Command Prompt
Navigate to the extracted directory:
```bash
cd ml_network_intrusion_detector
```

### Step 2: Create a Virtual Environment (Recommended)
- **Windows:**
  ```cmd
  python -m venv venv
  venv\Scripts\activate
  ```
- **macOS / Linux:**
  ```bash
  python3 -m venv venv
  source venv/bin/activate
  ```

### Step 3: Install Required Dependencies
```bash
pip install -r requirements.txt
```

---

## 🚀 Running the Project

### 1. Generate Dataset & Train Model
Run the pipeline to prepare data, train the Random Forest Classifier, and generate model artifacts:
```bash
python src/train_model.py
```

### 2. Run Inference Script
Test the trained model with sample network traffic input:
```bash
python src/predict.py
```

---

## 📊 Technical Stack
- **Language:** Python 3
- **Machine Learning:** Scikit-learn
- **Data Manipulation:** Pandas, NumPy
- **Model Serialization:** Joblib
