import scrapy
import json
import logging

from nbabasketball.parsers import NBATeamParser


class BalldontlieTeamSpider(scrapy.Spider):
    name = 'nbateamspider'
    custom_settings = {
        'ITEM_PIPELINES': {
            'nbabasketball.pipelines.NBATeamPipeline': 300,
        }
    }

    base_url = 'https://balldontlie.io/api/v1'
    team_url = f'{base_url}/teams'
    start_urls = [team_url]

    def __init__(self, *args, **kwargs):
        # Setup logging
        logger = logging.getLogger(__name__)
        logger.setLevel(logging.ERROR)
        super().__init__(*args, **kwargs)

    def parse(self, response):
        data = json.loads(response.body)

        # Parse info from page
        request_url = self.team_url
        for team_data in data['data']:
            yield NBATeamParser(team_data).output()

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
