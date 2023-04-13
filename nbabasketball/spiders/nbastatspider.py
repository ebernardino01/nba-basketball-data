import scrapy
import json
import logging

from nbabasketball.parsers import NBAStatParser


class BalldontlieStatSpider(scrapy.Spider):
    name = 'nbastatspider'
    custom_settings = {
        'ITEM_PIPELINES': {
            'nbabasketball.pipelines.NBAStatPipeline': 600,
        }
    }

    base_url = 'https://balldontlie.io/api/v1'
    stat_url = f'{base_url}/stats?seasons[]=2022&postseason=false'
    start_urls = [stat_url]

    def __init__(self, *args, **kwargs):
        # Setup logging
        logger = logging.getLogger(__name__)
        logger.setLevel(logging.ERROR)
        super().__init__(*args, **kwargs)

    def parse(self, response):
        data = json.loads(response.body)

        # Parse info from page
        request_url = self.stat_url
        for stat_data in data['data']:
            yield NBAStatParser(stat_data).output()

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
