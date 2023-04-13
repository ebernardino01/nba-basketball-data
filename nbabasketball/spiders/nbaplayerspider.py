import scrapy
import json
import logging

from nbabasketball.parsers import NBAPlayerParser


class BalldontliePlayerSpider(scrapy.Spider):
    name = 'nbaplayerspider'
    custom_settings = {
        'ITEM_PIPELINES': {
            'nbabasketball.pipelines.NBAPlayerPipeline': 400,
        }
    }

    base_url = 'https://balldontlie.io/api/v1'
    player_url = f'{base_url}/players'
    start_urls = [player_url]

    def __init__(self, *args, **kwargs):
        # Setup logging
        logger = logging.getLogger(__name__)
        logger.setLevel(logging.ERROR)
        super().__init__(*args, **kwargs)

    def parse(self, response):
        data = json.loads(response.body)

        # Parse info from page
        request_url = self.player_url
        for player_data in data['data']:
            yield NBAPlayerParser(player_data).output()

        # Check and parse meta info if there are additional pages
        if 'meta' in data:
            if 'next_page' in data['meta']:
                if data['meta']['next_page'] is not None:
                    print(response.url)
                    # Retrieve the url and fire request for the next page
                    page_arg = f"page={data['meta']['next_page']}"
                    matches = ['games', 'stats']
                    if any([identifier in request_url for identifier in matches]):
                        url = f"{request_url}&{page_arg}"
                    else:
                        url = f"{request_url}?{page_arg}"
                    yield scrapy.Request(url, self.parse)
