#!/bin/bash

export PATH=$PATH:/usr/local/bin:$HOME/.local/bin
DATE_WITH_TIME=`date "+%Y%m%dT%H%M%S"`
poetry run scrapy runspider nba_players.py --logfile logs/nbaplayerspider-${DATE_WITH_TIME}.log
