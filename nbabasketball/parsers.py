from nbabasketball.items import (
    NBATeamItem,
    NBAPlayerItem,
    NBAGameItem,
    NBAStatItem
)


class NBATeamParser:
    def output(self, item_json):
        team_item = NBATeamItem()
        team_item['id'] = item_json['id']
        team_item['abbreviation'] = item_json['abbreviation']
        team_item['city'] = item_json['city']
        team_item['conference'] = item_json['conference']
        team_item['division'] = item_json['division']
        team_item['full_name'] = item_json['full_name']
        team_item['name'] = item_json['name']
        return team_item


class NBAPlayerParser:
    def output(self, item_json):
        player_item = NBAPlayerItem()
        player_item['id'] = item_json['id']
        player_item['first_name'] = item_json['first_name']
        player_item['height_feet'] = item_json['height_feet']
        player_item['height_inches'] = item_json['height_inches']
        player_item['last_name'] = item_json['last_name']
        player_item['position'] = item_json['position']
        player_item['weight_pounds'] = item_json['weight_pounds']
        player_item['team_id'] = item_json['team']['id']
        return player_item


class NBAGameParser:
    def output(self, item_json):
        game_item = NBAGameItem()
        game_item['id'] = item_json['id']
        game_item['date'] = item_json['date']
        game_item['home_team_score'] = item_json['home_team_score']
        game_item['period'] = item_json['period']
        game_item['postseason'] = item_json['postseason']
        game_item['season'] = item_json['season']
        game_item['status'] = item_json['status']
        game_item['time'] = item_json['time']
        game_item['visitor_team_score'] = item_json['visitor_team_score']
        game_item['home_team_id'] = item_json['home_team']['id']
        game_item['visitor_team_id'] = item_json['visitor_team']['id']
        return game_item


class NBAStatParser:
    def output(self, item_json):
        stat_item = NBAStatItem()
        stat_item['id'] = item_json['id']
        stat_item['assists'] = item_json['ast']
        stat_item['blocks'] = item_json['blk']
        stat_item['defensive_rebounds'] = item_json['dreb']
        stat_item['field_goal_percent_3pt'] = item_json['fg3_pct']
        stat_item['field_goal_attempt_3pt'] = item_json['fg3a']
        stat_item['field_goal_made_3pt'] = item_json['fg3m']
        stat_item['field_goal_percent_2pt'] = item_json['fg_pct']
        stat_item['field_goal_attempt_2pt'] = item_json['fga']
        stat_item['field_goal_made_2pt'] = item_json['fgm']
        stat_item['free_throw_percent'] = item_json['ft_pct']
        stat_item['free_throw_attempt'] = item_json['fta']
        stat_item['free_throw_made'] = item_json['ftm']
        stat_item['minutes'] = item_json['min']
        stat_item['offensive_rebounds'] = item_json['oreb']
        stat_item['personal_fouls'] = item_json['pf']
        stat_item['points'] = item_json['pts']
        stat_item['rebounds'] = item_json['reb']
        stat_item['steals'] = item_json['stl']
        stat_item['turnovers'] = item_json['turnover']
        stat_item['game_id'] = item_json['game']['id']
        stat_item['player_id'] = item_json['player']['id']
        stat_item['team_id'] = item_json['team']['id']
        return stat_item
