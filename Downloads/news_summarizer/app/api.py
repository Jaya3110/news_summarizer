from flask import Flask, request, jsonify
from utils.scraper import extract_articles
from utils.tts import generate_hindi_audio
from werkzeug.serving import WSGIRequestHandler

# Set HTTP/1.1 for better performance
WSGIRequestHandler.protocol_version = "HTTP/1.1"

app = Flask(__name__)

@app.route('/')
def home():
    return "API is working!"

@app.route('/api/analyze', methods=['POST'])
def analyze_news():
    # Get data from request
    data = request.json
    company_name = data.get('company')
    
    # Check if company name is provided
    if not company_name:
        return jsonify({'error': 'Company name required'}), 400

    # Extract articles related to the company
    articles = extract_articles(company_name)
    
    # Generate text summary of articles
    summary_report = generate_summary_report(articles)
    
    # Ensure summary_report is a string
    if not isinstance(summary_report, str):
        summary_report = str(summary_report)

    # Generate Hindi audio summary
    hindi_audio_path = generate_hindi_audio(summary_report)

    return jsonify({"success": True, "report": summary_report, "audio_path": hindi_audio_path})

def generate_summary_report(articles):
    # Generate a text summary as a string
    summary = "Summary of articles:\n"
    for article in articles:
        summary += f"- {article['title']}: {article['summary']}\n"
    
    # Convert to string if it's not already a string
    if not isinstance(summary, str):
        summary = str(summary)

    return summary


if __name__ == '__main__':
    app.run(debug=True, threaded=True, port=5000)
