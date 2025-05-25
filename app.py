from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
from textblob import TextBlob

app = Flask(__name__)
CORS(app)

# Load model and vectorizer
model = joblib.load('fake_news_model.pkl')
vectorizer = joblib.load('tfidf_vectorizer.pkl')

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.get_json()
    news = data.get('news', '')

    if not news.strip():
        return jsonify({'error': 'News content is empty'}), 400

    vect_text = vectorizer.transform([news])
    prediction = model.predict(vect_text)[0]

    sentiment_score = TextBlob(news).sentiment.polarity
    sentiment = "Positive" if sentiment_score > 0 else "Negative" if sentiment_score < 0 else "Neutral"

    return jsonify({
        'status': 'Fake' if prediction == 0 else 'True',
        'sentiment': sentiment
    })

if __name__ == '__main__':
    app.run()
# Run the Flask app

