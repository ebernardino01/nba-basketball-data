import logging

from twisted.internet import reactor
from scrapy.crawler import CrawlerRunner
from scrapy.utils.project import get_project_settings

from spiders.nbateamspider import BalldontlieTeamSpider


logger = logging.getLogger(__name__)
logger.setLevel(logging.ERROR)


class NbaTeamSpider(BalldontlieTeamSpider):
    base_url = 'https://balldontlie.io/api/v1'
    start_urls = [f'{base_url}/teams']


runner = CrawlerRunner(settings=get_project_settings())
d = runner.crawl(NbaTeamSpider)
d.addBoth(lambda _: reactor.stop())
reactor.run() # the script will block here until the crawling is finished
