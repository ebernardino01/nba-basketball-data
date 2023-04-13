#!/bin/bash

export PATH=$PATH:/usr/local/bin:$HOME/.local/bin
DATE_WITH_TIME=`date "+%Y%m%dT%H%M%S"`
poetry run scrapy runspider nba_teams.py --logfile logs/nbateamspider-${DATE_WITH_TIME}.log
