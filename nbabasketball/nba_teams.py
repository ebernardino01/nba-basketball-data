import logging

from common import run_spider
from spiders.nbateamspider import BalldontlieTeamSpider


logger = logging.getLogger(__name__)
logger.setLevel(logging.ERROR)


class NbaTeamSpider(BalldontlieTeamSpider):
    base_url = 'https://balldontlie.io/api/v1'
    start_urls = [f'{base_url}/teams']


if __name__ == '__main__':
    run_spider(NbaTeamSpider)
