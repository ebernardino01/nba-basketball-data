# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field


class NBATeamItem(Item):
    id = Field()
    abbreviation = Field()
    city = Field()
    conference = Field()
    division = Field()
    full_name = Field()
    name = Field()


class NBAPlayerItem(Item):
    id = Field()
    first_name = Field()
    height_feet = Field()
    height_inches = Field()
    last_name = Field()
    position = Field()
    weight_pounds = Field()
    team_id = Field()


class NBAGameItem(Item):
    id = Field()
    date = Field()
    home_team_score = Field()
    period = Field()
    postseason = Field()
    season = Field()
    status = Field()
    time = Field()
    visitor_team_score = Field()
    home_team_id = Field()
    visitor_team_id = Field()


class NBAStatItem(Item):
    id = Field()
    assists = Field()
    blocks = Field()
    defensive_rebounds = Field()
    field_goal_percent_3pt = Field()
    field_goal_attempt_3pt = Field()
    field_goal_made_3pt = Field()
    field_goal_percent_2pt = Field()
    field_goal_attempt_2pt = Field()
    field_goal_made_2pt = Field()
    free_throw_percent = Field()
    free_throw_attempt = Field()
    free_throw_made = Field()
    minutes = Field()
    offensive_rebounds = Field()
    personal_fouls = Field()
    points = Field()
    rebounds = Field()
    steals = Field()
    turnovers = Field()
    game_id = Field()
    player_id = Field()
    team_id = Field()
