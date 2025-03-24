import requests
from bs4 import BeautifulSoup
from transformers import pipeline
import nltk
from nltk.corpus import stopwords
import re

nltk.download('stopwords')
stop_words = set(stopwords.words('english'))

# Summarization Model
summarizer = pipeline('summarization')

# Scrape and extract article content
def extract_articles(query):
    search_url = f"https://news.google.com/search?q={query}&hl=en"
    response = requests.get(search_url)
    soup = BeautifulSoup(response.text, 'html.parser')

    articles = []
    for item in soup.find_all('article', limit=10):
        title = item.find('h3').text if item.find('h3') else "No Title"
        link = item.find('a')['href'] if item.find('a') else "#"
        url = f"https://news.google.com{link[1:]}"
        content = extract_article_content(url)
        if content:
            summary, topics = summarize_article(content)
            sentiment = analyze_sentiment(content)
            articles.append({
                "Title": title,
                "Summary": summary,
                "Sentiment": sentiment,
                "Topics": topics,
                "URL": url
            })
    return articles


# Extract article content from the URL
def extract_article_content(url):
    try:
        article_page = requests.get(url)
        article_soup = BeautifulSoup(article_page.content, 'html.parser')
        paragraphs = article_soup.find_all('p')
        content = ' '.join([p.text for p in paragraphs])
        return content if content else None
    except:
        return None


# Summarize the content and extract topics
def summarize_article(content):
    summary = summarizer(content, max_length=100, min_length=30, do_sample=False)[0]['summary_text']
    words = re.findall(r'\w+', content.lower())
    topics = list(set([word for word in words if word not in stop_words and len(word) > 3]))
    return summary, topics


# Basic Sentiment Analysis
def analyze_sentiment(content):
    positive_words = ['good', 'great', 'positive', 'success', 'benefit', 'improve']
    negative_words = ['bad', 'worse', 'fail', 'down', 'negative', 'loss']

    pos_count = sum(1 for word in content.lower().split() if word in positive_words)
    neg_count = sum(1 for word in content.lower().split() if word in negative_words)

    if pos_count > neg_count:
        return 'Positive'
    elif neg_count > pos_count:
        return 'Negative'
    else:
        return 'Neutral'
