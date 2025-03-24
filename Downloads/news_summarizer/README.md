# 📚 News Summarizer and Hindi TTS API

A Flask-based API that extracts news articles about a company, performs sentiment and comparative analysis, and generates a Hindi audio summary using Google Text-to-Speech (gTTS).

---

## 🚀 Project Overview

This project extracts news articles related to a given company name, summarizes the content, performs sentiment and comparative analysis, and converts the summary to Hindi audio. The API is built using Flask and integrates multiple utilities for scraping, text analysis, and TTS generation.

---

## 📂 Folder Structure
/news_summarizer/ ├── /app/ │ ├── /utils/ │ │ ├── scraper.py # Extracts articles using BeautifulSoup │ │ ├── sentiment.py # Sentiment analysis and comparison │ │ └── tts.py # Hindi audio generation using gTTS │ ├── app.py # Main Flask API file │ ├── requirements.txt # Python dependencies │ └── README.md # Documentation ├── /templates/ │ └── index.html # (Optional) Frontend page └── /data/ └── output/ # Stores generated audio files


---

## ⚙️ Installation Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/Jaya3110/news_summarizer
cd news_summarizer/app

2. Create a Virtual Environment
# Create virtual environment
python -m venv env

# Activate virtual environment
# On Windows
env\Scripts\activate
# On Mac/Linux
source env/bin/activate

3.Install Dependencies
pip install -r requirements.txt


Running the Application
Run the Flask API:
python app.py
The API will be accessible at:
http://127.0.0.1:5000

 API Endpoints
1. Check API Status
GET /
Response: "API is working!"
2. Analyze News and Generate Hindi Audio
POST /api/analyze
Content-Type: application/json
Body:
{
  "company": "Tesla"
}
Response:
{
  "success": true,
  "report": "Summary of articles...",
  "audio_path": "output/audio.mp3"
}


Example Usage
Using cURL

curl -X POST -H "Content-Type: application/json" -d '{"company": "Tesla"}' http://127.0.0.1:5000/api/analyze
Using Postman
URL: http://127.0.0.1:5000/api/analyze

Method: POST

Body:
{
  "company": "Tesla"
}

Audio Output
Hindi audio summary is saved in the /data/output/ folder.

Example path: output/audio.mp3

📜 Code Overview
1. app.py
Main Flask application.
Handles API requests and routes.

2. /utils/scraper.py
Extracts articles using BeautifulSoup.
Returns a list of article summaries.

3. /utils/sentiment.py
Analyzes the sentiment and performs a comparative analysis.

Generates a summarized sentiment report.

4. /utils/tts.py
Converts the generated text summary to Hindi audio.

Saves the audio file in output/ directory.

📦 Packaging for Submission
1. Zip the Project Folder
zip -r news_summarizer.zip news_summarizer/
2. Verify Folder Contents
Ensure the ZIP contains: ✅ Code
✅ requirements.txt
✅ README.md
✅ Sample Output (Audio + JSON response)

📝 Sample Response
{
  "success": true,
  "report": "Summary of articles related to Tesla...",
  "audio_path": "output/audio.mp3"
}
