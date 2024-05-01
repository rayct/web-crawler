# app.py
from crawler.web_crawler import WebCrawler

def main():
    # Instantiate the WebCrawler with the URL file
    url_file = "urls.txt"
    crawler = WebCrawler(url_file)

    # Start crawling
    crawler.crawl()

if __name__ == "__main__":
    main()
