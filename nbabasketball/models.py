from dotenv import dotenv_values

from sqlalchemy import create_engine, Column, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import BOOLEAN
from sqlalchemy.dialects.mysql.types import (
    BIGINT,
    DATETIME,
    DECIMAL,
    SMALLINT,
    TINYINT,
    VARCHAR
)


env = dotenv_values('.env')
Base = declarative_base()


def db_connect():
    """
    Performs database connection using database settings from settings.py
    Returns sqlalchemy engine instance
    """
    return create_engine(
        env.get('DATABASE_URL'),
        pool_size=30,
        max_overflow=0
    )


def create_table(engine):
    """
    Create all tables stored in this metadata.
    Conditional by default, will not attempt to recreate tables already present in the target database.

    :param engine: connectable to access the database
    """
    Base.metadata.create_all(engine)


class NBATeam(Base):
    __tablename__ = "nba_teams"

    id = Column(BIGINT, primary_key=True)
    abbreviation = Column('abbreviation', VARCHAR(3))
    city = Column('city', VARCHAR(100))
    conference = Column('conference', VARCHAR(50))
    division = Column('division', VARCHAR(50))
    full_name = Column('full_name', VARCHAR(100))
    name = Column('name', VARCHAR(100))
    scraped_date_time = Column('scraped_date_time', DATETIME)

    players = relationship(
        'NBAPlayer',
        primaryjoin='(NBATeam.id == NBAPlayer.team_id)'
    )
    games = relationship(
        'NBAGame',
        primaryjoin='or_(NBATeam.id == NBAGame.home_team_id, NBATeam.id == NBAGame.visitor_team_id)',
        backref='team'
    )
    stats = relationship(
        'NBAStat',
        primaryjoin='(NBATeam.id == NBAStat.team_id)',
        backref='team'
    )


class NBAPlayer(Base):
    __tablename__ = "nba_players"

    id = Column(BIGINT, primary_key=True)
    first_name = Column('first_name', VARCHAR(255))
    height_feet = Column('height_feet', SMALLINT)
    height_inches = Column('height_inches', SMALLINT)
    last_name = Column('last_name', VARCHAR(255))
    position = Column('position', VARCHAR(100))
    weight_pounds = Column('weight_pounds', SMALLINT)
    scraped_date_time = Column('scraped_date_time', DATETIME)

    team_id = Column(BIGINT, ForeignKey('nba_teams.id'))
    team = relationship(
        'NBATeam',
        foreign_keys=[team_id],
        overlaps='players'
    )


class NBAGame(Base):
    __tablename__ = "nba_games"

    id = Column(BIGINT, primary_key=True)
    date = Column('date', DATETIME)
    home_team_score = Column('home_team_score', SMALLINT)
    period = Column('period', TINYINT)
    postseason = Column('postseason', BOOLEAN)
    season = Column('season', SMALLINT)
    status = Column('status', VARCHAR(50))
    time = Column('time', VARCHAR(50))
    visitor_team_score = Column('visitor_team_score', SMALLINT)
    scraped_date_time = Column('scraped_date_time', DATETIME)

    home_team_id = Column(BIGINT, ForeignKey('nba_teams.id'))
    home_team = relationship(
        'NBATeam',
        foreign_keys=[home_team_id],
        overlaps='games,team'
    )
    visitor_team_id = Column(BIGINT, ForeignKey('nba_teams.id'))
    visitor_team = relationship(
        'NBATeam',
        foreign_keys=[visitor_team_id],
        overlaps='games,team'
    )


class NBAStat(Base):
    __tablename__ = "nba_stats"

    id = Column(BIGINT, primary_key=True)
    assists = Column('assists', SMALLINT)
    blocks = Column('blocks', SMALLINT)
    defensive_rebounds = Column('defensive_rebounds', SMALLINT)
    field_goal_percent_3pt = Column('field_goal_percent_3pt', DECIMAL(5,2))
    field_goal_attempt_3pt = Column('field_goal_attempt_3pt', SMALLINT)
    field_goal_made_3pt = Column('field_goal_made_3pt', SMALLINT)
    field_goal_percent_2pt = Column('field_goal_percent_2pt', DECIMAL(5,2))
    field_goal_attempt_2pt = Column('field_goal_attempt_2pt', SMALLINT)
    field_goal_made_2pt = Column('field_goal_made_2pt', SMALLINT)
    free_throw_percent = Column('free_throw_percent', DECIMAL(5,2))
    free_throw_attempt = Column('free_throw_attempt', SMALLINT)
    free_throw_made = Column('free_throw_made', SMALLINT)
    minutes = Column('minutes', TINYINT)
    offensive_rebounds = Column('offensive_rebounds', SMALLINT)
    personal_fouls = Column('personal_fouls', TINYINT)
    points = Column('points', SMALLINT)
    rebounds = Column('rebounds', SMALLINT)
    steals = Column('steals', SMALLINT)
    turnovers = Column('turnovers', SMALLINT)
    scraped_date_time = Column('scraped_date_time', DATETIME)

    game_id = Column(BIGINT, ForeignKey('nba_games.id'))
    player_id = Column(BIGINT, ForeignKey('nba_players.id'))
    team_id = Column(BIGINT, ForeignKey('nba_teams.id'))
