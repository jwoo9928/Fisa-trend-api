import requests
from bs4 import BeautifulSoup

def get_realtime_search_terms():
    url = "https://www.google.com/trends/hottrends/atom/feed?pn=p1"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'xml')
    titles = soup.find_all('title')
    
    search_terms = [title.text for title in titles[1:11]]  # 첫 번째는 제목이므로 제외
    return search_terms

def update_readme(search_terms):
    with open("README.md", "w") as file:
        file.write("# 실시간 검색어 Top 10\n\n")
        for i, term in enumerate(search_terms, 1):
            file.write(f"{i}. {term}\n")

if __name__ == "__main__":
    search_terms = get_realtime_search_terms()
    update_readme(search_terms)