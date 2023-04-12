import scrapy
import json
import logging

from nbabasketball.parsers import (
    NBATeamParser,
    NBAPlayerParser,
    NBAGameParser,
    NBAStatParser
)


class NbaspiderSpider(scrapy.Spider):
    name = 'nbaspider'

    base_url = 'https://balldontlie.io/api/v1'
    team_url = f'{base_url}/teams'
    player_url = f'{base_url}/players'
    game_url = f'{base_url}/games?seasons[]=2022'
    stat_url = f'{base_url}/stats?seasons[]=2022'
    start_urls = [
        team_url, player_url, game_url, stat_url
    ]

    def __init__(self, *args, **kwargs):
        # Setup logging
        logger = logging.getLogger(__name__)
        logger.setLevel(logging.ERROR)
        super().__init__(*args, **kwargs)

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url, self.parse)

    def parse(self, response):
        data = json.loads(response.body)

        # Parse info from page
        if 'teams' in response.url:
            for team_data in data['data']:
                yield NBATeamParser(team_data).output()
        elif 'players' in response.url:
            for player_data in data['data']:
                yield NBAPlayerParser(player_data).output()
        elif 'games' in response.url:
            for game_data in data['data']:
                yield NBAGameParser(game_data).output()
        elif 'stats' in response.url:
            for stat_data in data['data']:
                yield NBAStatParser(stat_data).output()

        # Check and parse meta info if there are additional pages
        if 'meta' in data:
            if data['next_page'] is not None:
                # Retrieve the url and fire request for the next page
                page_arg = f"page={data['next_page']}"
                matches = ['games', 'stats']
                if any([identifier in response.url for identifier in matches]):
                    url = f"{response.url}&{page_arg}"
                else:
                    url = f"{response.url}?{page_arg}"
                yield scrapy.Request(url, self.parse)
