
# Sentiment Analysis for Fake News Propagation

## 📰 Overview

This project combines **Fake News Detection** with **Sentiment Analysis** to not only determine whether a news article is fake or real, but also understand the emotional tone (positive, negative, or neutral) it conveys.

With the rise of misinformation, analyzing both **credibility** and **sentiment** can help in understanding the impact of news on public opinion.

---

## 🚀 Features

- ✅ Fake News Detection using machine learning and TF-IDF.
- 😊 Sentiment Analysis using TextBlob.
- 🔐 Text security via AES Encryption and SHA-256 Hashing.
- 🌐 Interactive frontend built with HTML, CSS, and JavaScript.
- 🔗 Flask-powered backend providing a REST API.

---

## 📌 Project Approach

The project is developed in two main phases:

1. **Fake News Detection**  
   - Collected two datasets: `Fake.csv` and `True.csv`.
   - Cleaned and preprocessed the data using regular expressions and string manipulation (lowercasing, punctuation removal, etc.).
   - Applied **TF-IDF vectorization** to convert text into numerical features.
   - Trained multiple ML models (Logistic Regression, Passive Aggressive Classifier, etc.).
   - Evaluated performance using accuracy, confusion matrices, and classification reports.

2. **Sentiment Analysis**  
   - Reused the preprocessing pipeline from the fake news system.
   - Integrated sentiment-labeled datasets or inferred sentiment from the existing news dataset.
   - Applied **TextBlob** for sentiment polarity detection.
   - Added AES encryption to secure the text content and SHA-256 hashing to verify data integrity.

This modular design allows the system to be easily adapted for additional NLP tasks such as emotion detection, media bias analysis, or topic classification.

---

## 🧠 How It Works (Workflow)

### Step-by-Step Workflow

1. **User Input**
   - A user submits a news article through the web interface.

2. **Preprocessing**
   - The text is cleaned using custom functions (removing punctuation, lowercasing, etc.).
   - Transformed into numerical form using the stored **TF-IDF vectorizer**.

3. **Prediction**
   - The cleaned text is passed to a saved ML model to classify it as **Fake** or **Real**.
   - Simultaneously, **TextBlob** is used to analyze the **sentiment polarity** of the article.

4. **Security Layer**
   - The text content is **encrypted using AES** before transmission or storage.
   - A **SHA-256 hash** is generated for verification purposes.

5. **Output Display**
   - Results are returned to the frontend and displayed as:
     - **News Status:** Fake or Real
     - **Sentiment:** Positive, Negative, or Neutral

---

## 🧾 Example Output

```
News Status: Fake
Sentiment: Negative
```

---

## 🗂 Project Structure

```
Sentiment-Analysis-For-Fake-News-Propagation/
│
├── Fake_News_Detection.ipynb                  # Initial fake news detection model
├── Fake_News_Detection_with_Sentiment.ipynb   # Enhanced version with sentiment analysis
├── app.py                                     # Flask backend API
├── fake_news_model.pkl                        # Trained ML model
├── tfidf_vectorizer.pkl                       # TF-IDF vectorizer used in training
├── requirements.txt                           # Python dependencies
├── README.md                                  # Project documentation
│
└── frontend/
    ├── index.html                             # Web interface
    └── style.css                              # Styling for UI
```

---

## 🛠️ Technologies Used

- **Python**, **Flask**
- **scikit-learn**, **TextBlob**, **joblib**
- **pycryptodome** for AES encryption
- **hashlib** for SHA-256
- **HTML**, **CSS**, **JavaScript**
- **TF-IDF** for feature extraction

---

## 👥 Authors

- **Shreya Agarwal** – [shreyaagarwal0015@gmail.com](mailto:shreyaagarwal0015@gmail.com)
- **Sristee Agrawal** – [agrawalsristee12@gmail.com](mailto:agrawalsristee12@gmail.com)

---
