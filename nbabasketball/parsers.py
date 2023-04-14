from datetime import datetime
from dateutil.parser import parse

from nbabasketball.items import (
    NBATeamItem,
    NBAPlayerItem,
    NBAGameItem,
    NBAStatItem
)


class BaseParser:
    """ Base parser class """
    def __init__(self, parse_json) -> None:
        self.item_json = parse_json


class NBATeamParser(BaseParser):
    def output(self):
        team_item = NBATeamItem()
        team_item['id'] = self.item_json['id']
        team_item['abbreviation'] = self.item_json['abbreviation']
        team_item['city'] = self.item_json['city']
        team_item['conference'] = self.item_json['conference']
        team_item['division'] = self.item_json['division']
        team_item['full_name'] = self.item_json['full_name']
        team_item['name'] = self.item_json['name']
        team_item['scraped_date_time'] = datetime.now()
        return team_item


class NBAPlayerParser(BaseParser):
    def output(self):
        player_item = NBAPlayerItem()
        player_item['id'] = self.item_json['id']
        player_item['first_name'] = self.item_json['first_name']
        player_item['height_feet'] = self.item_json['height_feet']
        player_item['height_inches'] = self.item_json['height_inches']
        player_item['last_name'] = self.item_json['last_name']
        player_item['position'] = self.item_json['position']
        player_item['weight_pounds'] = self.item_json['weight_pounds']
        player_item['team_id'] = self.item_json['team']['id']
        player_item['scraped_date_time'] = datetime.now()
        return player_item


class NBAGameParser(BaseParser):
    def output(self):
        game_item = NBAGameItem()
        game_item['id'] = self.item_json['id']
        game_item['date'] = parse(self.item_json['date'])
        game_item['home_team_score'] = self.item_json['home_team_score']
        game_item['period'] = self.item_json['period']
        game_item['postseason'] = self.item_json['postseason']
        game_item['season'] = self.item_json['season']
        game_item['status'] = self.item_json['status']
        game_item['time'] = self.item_json['time']
        game_item['visitor_team_score'] = self.item_json['visitor_team_score']
        game_item['home_team_id'] = self.item_json['home_team']['id']
        game_item['visitor_team_id'] = self.item_json['visitor_team']['id']
        game_item['scraped_date_time'] = datetime.now()
        return game_item


class NBAStatParser(BaseParser):
    def output(self):
        stat_item = NBAStatItem()
        stat_item['stat_id'] = self.item_json['id']
        stat_item['assists'] = self.item_json['ast']
        stat_item['blocks'] = self.item_json['blk']
        stat_item['defensive_rebounds'] = self.item_json['dreb']
        stat_item['field_goal_percent_3pt'] = self.item_json['fg3_pct']
        stat_item['field_goal_attempt_3pt'] = self.item_json['fg3a']
        stat_item['field_goal_made_3pt'] = self.item_json['fg3m']
        stat_item['field_goal_percent_2pt'] = self.item_json['fg_pct']
        stat_item['field_goal_attempt_2pt'] = self.item_json['fga']
        stat_item['field_goal_made_2pt'] = self.item_json['fgm']
        stat_item['free_throw_percent'] = self.item_json['ft_pct']
        stat_item['free_throw_attempt'] = self.item_json['fta']
        stat_item['free_throw_made'] = self.item_json['ftm']
        stat_item['minutes'] = self.item_json['min']
        stat_item['offensive_rebounds'] = self.item_json['oreb']
        stat_item['personal_fouls'] = self.item_json['pf']
        stat_item['points'] = self.item_json['pts']
        stat_item['rebounds'] = self.item_json['reb']
        stat_item['steals'] = self.item_json['stl']
        stat_item['turnovers'] = self.item_json['turnover']
        stat_item['game_id'] = self.item_json['game']['id']
        stat_item['player_id'] = self.item_json['player']['id']
        stat_item['team_id'] = self.item_json['team']['id']
        stat_item['scraped_date_time'] = datetime.now()
        return stat_item
