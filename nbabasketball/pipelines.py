# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import logging
from scrapy import Spider
from sqlalchemy.orm import sessionmaker

from nbabasketball.models import (
    db_connect,
    create_table,
    NBATeam,
    NBAPlayer,
    NBAGame,
    NBAStat
)


logger = logging.getLogger(__name__)
logger.setLevel(logging.ERROR)


class NbabasketballPipeline:
    def __init__(self):
        """
        Initialize database connection and sessionmaker
        Create database tables
        """
        self.rows = []
        try:
            engine = db_connect()
            create_table(engine)
            self.Session = sessionmaker(bind=engine)
            print(self.Session)
        except Exception as e:
            logger.error('Connection problem: ', e.args)


    def close_spider(self, spider: Spider) -> None:
        """
        Saving all the scraped events in bulk on spider close event
        """
        session = self.Session()
        try:
            logger.info('Saving events in bulk operation to the database...')
            session.add_all(self.rows)
            session.commit()
        except Exception as error:
            logger.exception(error, extra=dict(spider=spider))
            session.rollback()
            raise
        finally:
            session.close()


class NBATeamPipeline(NbabasketballPipeline):
    def process_item(self, item, spider: Spider):
        """
        Processes every item pipeline component for the team
        """
        session = self.Session()
        try:
            existing_team = session.query(NBATeam).filter_by(
                id=item['id']
            ).first()

            # Check for instance before adding
            if not existing_team:
                team_item = NBATeam()
                team_item.id = item['id']
                team_item.abbreviation = item['abbreviation']
                team_item.city = item['city']
                team_item.conference = item['conference']
                team_item.division = item['division']
                team_item.full_name = item['full_name']
                team_item.name = item['name']
                team_item.scraped_date_time = item['scraped_date_time']
                self.rows.append(team_item)
        finally:
            session.close()

        return item


class NBAPlayerPipeline(NbabasketballPipeline):
    def process_item(self, item, spider: Spider):
        """
        Processes every item pipeline component for the player
        """
        session = self.Session()
        try:
            existing_player = session.query(NBAPlayer).filter_by(
                id=item['id']
            ).first()

            # Check for instance before adding
            if not existing_player:
                player_item = NBAPlayer()
                player_item.id = item['id']
                player_item.first_name = item['first_name']
                player_item.height_feet = item['height_feet']
                player_item.height_inches = item['height_inches']
                player_item.last_name = item['last_name']
                player_item.position = item['position']
                player_item.weight_pounds = item['weight_pounds']
                player_item.team_id = item['team_id']
                player_item.scraped_date_time = item['scraped_date_time']
                self.rows.append(player_item)
        finally:
            session.close()

        return item


class NBAGamePipeline(NbabasketballPipeline):
    def process_item(self, item, spider: Spider):
        """
        Processes every item pipeline component for the game
        """
        session = self.Session()
        try:
            existing_game = session.query(NBAGame).filter_by(
                id=item['id']
            ).first()

            # Check for instance before adding
            if not existing_game:
                game_item = NBAGame()
                game_item.id = item['id']
                game_item.date = item['date']
                game_item.home_team_score = item['home_team_score']
                game_item.period = item['period']
                game_item.postseason = item['postseason']
                game_item.season = item['season']
                game_item.status = item['status']
                game_item.time = item['time']
                game_item.visitor_team_score = item['visitor_team_score']
                game_item.home_team_id = item['home_team_id']
                game_item.visitor_team_id = item['visitor_team_id']
                game_item.scraped_date_time = item['scraped_date_time']
                self.rows.append(game_item)
        finally:
            session.close()

        return item


class NBAStatPipeline(NbabasketballPipeline):
    def process_item(self, item, spider: Spider):
        """
        Processes every item pipeline component for the stat
        """
        session = self.Session()
        try:
            existing_stat = session.query(NBAStat).filter_by(
                stat_id=item['stat_id']
            ).first()

            # Check for instance before adding
            if not existing_stat:
                stat_item = NBAStat()
                stat_item.stat_id = item['stat_id']
                stat_item.assists = item['assists']
                stat_item.blocks = item['blocks']
                stat_item.defensive_rebounds = item['defensive_rebounds']
                stat_item.field_goal_percent_3pt = item['field_goal_percent_3pt']
                stat_item.field_goal_attempt_3pt = item['field_goal_attempt_3pt']
                stat_item.field_goal_made_3pt = item['field_goal_made_3pt']
                stat_item.field_goal_percent_2pt = item['field_goal_percent_2pt']
                stat_item.field_goal_attempt_2pt = item['field_goal_attempt_2pt']
                stat_item.field_goal_made_2pt = item['field_goal_made_2pt']
                stat_item.free_throw_percent = item['free_throw_percent']
                stat_item.free_throw_attempt = item['free_throw_attempt']
                stat_item.free_throw_made = item['free_throw_made']
                stat_item.minutes = item['minutes']
                stat_item.offensive_rebounds = item['offensive_rebounds']
                stat_item.personal_fouls = item['personal_fouls']
                stat_item.points = item['points']
                stat_item.rebounds = item['rebounds']
                stat_item.steals = item['steals']
                stat_item.turnovers = item['turnovers']
                stat_item.game_id = item['game_id']
                stat_item.player_id = item['player_id']
                stat_item.team_id = item['team_id']
                stat_item.scraped_date_time = item['scraped_date_time']
                self.rows.append(stat_item)
        finally:
            session.close()

        return item
