# web_crawler.py
import requests
from bs4 import BeautifulSoup
import os

class WebCrawler:
    def __init__(self, base_urls):
        self.base_urls = base_urls
        self.visited_urls = set()
        self.output_dir = os.path.join(os.path.dirname(__file__), '..', 'output')

    def crawl(self, max_depth=3):
        for base_url in self.base_urls:
            self._crawl_single_site(base_url, max_depth)

    def _crawl_single_site(self, base_url, max_depth):
        if max_depth == 0:
            return

        if base_url in self.visited_urls:
            return

        try:
            response = requests.get(base_url)
            if response.status_code == 200:
                self.visited_urls.add(base_url)
                self.parse_page(response.content)
                soup = BeautifulSoup(response.content, 'html.parser')
                for link in soup.find_all('a', href=True):
                    next_url = link['href']
                    if next_url.startswith('http'):
                        self._crawl_single_site(next_url, max_depth - 1)
                    elif next_url.startswith('/'):
                        next_url = base_url + next_url
                        self._crawl_single_site(next_url, max_depth - 1)
        except Exception as e:
            print(f"Error crawling {base_url}: {e}")

    def parse_page(self, content):
        soup = BeautifulSoup(content, 'html.parser')
        for img_tag in soup.find_all('img'):
            img_url = img_tag['src']
            self.download_image(img_url)

        text = soup.get_text()
        self.save_text(text)

    def download_image(self, img_url):
        try:
            img_response = requests.get(img_url)
            if img_response.status_code == 200:
                img_name = img_url.split('/')[-1]
                img_path = os.path.join(self.output_dir, img_name)
                with open(img_path, 'wb') as f:
                    f.write(img_response.content)
                print(f"Downloaded image: {img_name}")
        except Exception as e:
            print(f"Error downloading image from {img_url}: {e}")

    def save_text(self, text):
        try:
            text_path = os.path.join(self.output_dir, 'text_content.txt')
            with open(text_path, 'a') as f:
                f.write(text)
                f.write('\n')
            print("Text content saved.")
        except Exception as e:
            print(f"Error saving text content: {e}")

if __name__ == "__main__":
    # Example usage
    base_urls = ["https://rayturner.dev"]
    crawler = WebCrawler(base_urls)
    crawler.crawl()
