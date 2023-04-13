import logging

from twisted.internet import reactor, defer
from scrapy.crawler import CrawlerRunner
from scrapy.utils.project import get_project_settings

from spiders.nbastatspider import BalldontlieStatSpider


logger = logging.getLogger(__name__)
logger.setLevel(logging.ERROR)


class NbaStatSpider(BalldontlieStatSpider):
    base_url = 'https://balldontlie.io/api/v1'
    start_urls = [f'{base_url}/stats?seasons[]=2022&postseason=false']


runner = CrawlerRunner(settings=get_project_settings())
d = runner.crawl(NbaStatSpider)
d.addBoth(lambda _: reactor.stop())
reactor.run() # the script will block here until the crawling is finished
