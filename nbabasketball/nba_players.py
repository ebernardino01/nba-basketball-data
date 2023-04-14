import logging

from common import run_spider
from spiders.nbaplayerspider import BalldontliePlayerSpider


logger = logging.getLogger(__name__)
logger.setLevel(logging.ERROR)


class NbaPlayerSpider(BalldontliePlayerSpider):
    base_url = 'https://balldontlie.io/api/v1'
    start_urls = [f'{base_url}/players']


if __name__ == '__main__':
    run_spider(NbaPlayerSpider)
