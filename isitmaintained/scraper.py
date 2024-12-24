"""Scrapy spider to scrape health scores from a website."""

from typing import ClassVar

import scrapy
from bs4 import BeautifulSoup
from scrapy.crawler import CrawlerProcess
from scrapy.http import Response

from .logging_utils import logit


class HealthSpider(scrapy.Spider):
    """A Scrapy spider to scrape health scores from a website.

    Attributes:
        name (str): The name of the spider.
        start_urls (list): The initial URLs to start scraping from.
        health_score (str): The health score extracted from the webpage.

    Methods:
        parse(response):
            Parses the response from the webpage and extracts the health score.
    """

    start_urls: ClassVar[list] = []
    health_score = None

    @logit
    def parse(self, response: Response) -> None:
        """Parse the response to extract the health score.

        Args:
            response (scrapy.http): The HTTP response object to parse.

        Attributes:
            health_score (str): The extracted health score from the response.
        """
        soup = BeautifulSoup(response.body, "html.parser")
        health_score = soup.find("div", class_="score-bar__score").text.strip()
        self.health_score = health_score


@logit
def get_package_health(url: str) -> float:
    """Fetch the health score of a package from the given URL using a web crawler.

    Args:
        url (str): The URL of the package page to scrape.

    Returns:
        float: The health score of the package as determined by the HealthSpider.
    """
    process = CrawlerProcess(settings={"LOG_LEVEL": "ERROR"})
    spider = HealthSpider()
    spider.start_urls = [url]
    _ = process.crawl(spider)
    process.start()
    return spider.health_score


def scrape_table_from_url(url: str) -> str:
    """Scrape the first table from the given URL.

    Args:
        url (str): The URL of the page to scrape.

    Returns:
        str: The HTML content of the first table found on the page, or an empty string if no table is found.
    """
    process = CrawlerProcess(settings={"LOG_LEVEL": "ERROR"})
    table_html = []

    class TableSpider(scrapy.Spider):
        name = "table_spider"
        start_urls: ClassVar[list] = [url]

        @staticmethod
        def parse(response: Response) -> None:
            soup = BeautifulSoup(response.body, "html.parser")
            table = soup.find("table")
            if table:
                table_html.append(str(table))

    process.crawl(TableSpider)
    process.start()
    return table_html[0] if table_html else ""
