import logging

from twisted.internet import reactor
from scrapy.crawler import CrawlerRunner
from scrapy.utils.project import get_project_settings

from spiders.nbaplayerspider import BalldontliePlayerSpider


logger = logging.getLogger(__name__)
logger.setLevel(logging.ERROR)


class NbaPlayerSpider(BalldontliePlayerSpider):
    base_url = 'https://balldontlie.io/api/v1'
    start_urls = [f'{base_url}/players']


runner = CrawlerRunner(settings=get_project_settings())
d = runner.crawl(NbaPlayerSpider)
d.addBoth(lambda _: reactor.stop())
reactor.run() # the script will block here until the crawling is finished
