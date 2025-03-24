import requests

try:
    response = requests.get("https://translate.google.com/", timeout=5)
    if response.status_code == 200:
        print("✅ Internet is working. Google API is accessible.")
    else:
        print(f"⚠️ Google API returned status code: {response.status_code}")
except requests.ConnectionError:
    print("❌ No internet connection or Google API is blocked.")
