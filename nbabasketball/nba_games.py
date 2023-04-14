import logging

from common import run_spider
from spiders.nbagamespider import BalldontlieGameSpider


logger = logging.getLogger(__name__)
logger.setLevel(logging.ERROR)


class NbaGameSpider(BalldontlieGameSpider):
    base_url = 'https://balldontlie.io/api/v1'
    start_urls = [f'{base_url}/games?seasons[]=2022&postseason=false']


if __name__ == '__main__':
    run_spider(NbaGameSpider)
