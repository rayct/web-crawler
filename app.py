# app.py
from crawler.web_crawler import WebCrawler

def main():
    # Instantiate the WebCrawler
    crawler = WebCrawler()

    # Specify the base URLs to crawl
    base_urls = ["https://rayturner.dev", "https://tailoredscaffolding.co.uk"]

    # Start crawling from the specified URLs
    crawler.crawl_from_urls(base_urls)

if __name__ == "__main__":
    main()
