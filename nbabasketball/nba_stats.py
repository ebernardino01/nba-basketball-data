import logging

from common import run_spider
from spiders.nbastatspider import BalldontlieStatSpider


logger = logging.getLogger(__name__)
logger.setLevel(logging.ERROR)


class NbaStatSpider(BalldontlieStatSpider):
    base_url = 'https://balldontlie.io/api/v1'
    start_urls = [f'{base_url}/stats?seasons[]=2022&postseason=false']


if __name__ == '__main__':
    run_spider(NbaStatSpider)
