import requests
from bs4 import BeautifulSoup

def extract_course_links(url):
    try:
        r = requests.get(url, timeout=10)
        soup = BeautifulSoup(r.text, "html.parser")
        links = [a['href'] for a in soup.find_all('a', href=True)]
        return links
    except Exception as e:
        return [f"Error: {e}"]
      
