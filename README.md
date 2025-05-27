Sentiment Analysis for Fake News Propagation This project is a Fake News Detection system integrated with Sentiment Analysis. It uses a machine learning model to classify news as Fake or True and applies sentiment analysis to determine the emotional tone of the news content (Positive, Negative, or Neutral).

Project Overview Fake news spreads quickly and has serious consequences. This project aims to not only detect the authenticity of a news article but also analyze the sentiment it carries, helping users better understand the nature and potential impact of the content.

Features

Fake News Detection using TF-IDF vectorizer and trained ML model. Sentiment Analysis using TextBlob. Interactive Frontend built using HTML, CSS, and JavaScript. REST API powered by Flask backend.

Project Structure Sentiment-Analysis-For-Fake-News-Propagation/ │ ├── Fake_News_Detection.ipynb # Initial model development ├── Fake_News_Detection_with_Sentiment.ipynb # Enhanced version with sentiment analysis ├── app.py # Flask API for prediction ├── fake_news_model.pkl # Trained ML model ├── tfidf_vectorizer.pkl # TF-IDF vectorizer used in training ├── requirements.txt # Python dependencies ├── README.md # Project documentation ├── frontend/ │ ├── index.html # Frontend interface │ └── style.css # Styling for frontend

How It Works User pastes a news article into the web interface. The text is sent to the Flask backend. The backend: Transforms the input using the TF-IDF vectorizer. Uses the saved model to classify the news as Fake or True. Performs sentiment analysis using TextBlob. Results are displayed on the frontend.

Technologies Used Python, Flask scikit-learn, joblib, TextBlob HTML, CSS, JavaScript TF-IDF for feature extraction

Example Output News Status: Fake Sentiment: Negative

Author- @shreyaagarwal156 @SristeeAgrawal @AmolikaUniyal @dee-15
