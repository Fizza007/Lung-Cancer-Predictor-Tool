# Lung-Cancer-Predictor-Tool
Here’s a **README.md** for your GitHub repository based on the files and code you provided:

---

# 🩺 Lung-Cancer-Predictor-Tool

A **machine learning-powered Streamlit app** that predicts the risk of lung cancer based on patient data such as age, gender, smoking habits, and medical symptoms. The model is trained using Support Vector Classifier (SVC) with feature scaling and encoders for improved prediction accuracy.

---

## 🚀 Features

✅ Predicts lung cancer risk using patient details
✅ Provides probability score (%) for better risk assessment
✅ Simple and interactive **Streamlit UI**
✅ Uses pre-trained SVC model with scaler and encoders

---

## 📂 Repository Structure

```
├── LungCancer.csv           # Dataset used for training
├── app.py                   # Streamlit app code
├── encoder_gender.pkl       # Gender label encoder
├── encoder_lung.pkl         # Lung cancer label encoder
├── scaler.pkl               # Scaler for age normalization
├── svc_best_model.pkl       # Trained Support Vector Classifier model
├── requirements.txt         # Python dependencies
└── README.md                # Project documentation
```

---

## 🛠️ Installation & Setup

1️⃣ **Clone this repository:**

```bash
git clone https://github.com/Fizza007/Lung-Cancer-Predictor-Tool.git
cd Lung-Cancer-Predictor-Tool
```

2️⃣ **Create a virtual environment (recommended):**

```bash
python -m venv venv
source venv/bin/activate      # For Mac/Linux
venv\Scripts\activate         # For Windows
```

3️⃣ **Install dependencies:**

```bash
pip install -r requirements.txt
```

4️⃣ **Run the Streamlit app:**

```bash
streamlit run app.py
```

---

## 📊 Usage

* Open the app in your browser.
* Enter patient details (age, gender, symptoms, etc.).
* Click **Predict** to get:

  * ✅ **Risk classification (High/Low)**
  * 📊 **Probability of lung cancer (%)**

---

## 🤖 Model Information

* Algorithm: **Support Vector Classifier (SVC)**
* Preprocessing:

  * Label Encoding for gender & lung cancer
  * Feature Scaling for age
* Output:

  * `1` → High Risk of Lung Cancer
  * `0` → Low Risk of Lung Cancer

---

## 📦 Requirements

* Python 3.8+
* Streamlit
* NumPy
* Joblib
* Scikit-learn

(Already listed in `requirements.txt`)

---

## 📌 Future Enhancements

🔹 Add more clinical features for improved prediction accuracy
🔹 Deploy on cloud platforms (AWS / HuggingFace Spaces)
🔹 Integrate database for storing patient history

---

## 👩‍💻 Author

**Fizza Shahtaj**
📧 [fshahtaj1688@monroeu.edu](mailto:fshahtaj1688@monroeu.edu)
🔗 [LinkedIn](https://www.linkedin.com/in/fizza-s-4ba95a19a)


