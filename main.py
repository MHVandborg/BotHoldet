import pandas as pd
import numpy as np
import datetime as dt
import csv
from files.functions import *
from files.teams import *
        

# Load all matches
df = pd.read_csv('matches.csv', index_col=None)


# Variables
df = df[df['season'] == 2022]
date_current = dt.datetime(2022,8,24)
rounds = 1
decimals = 1e2
league = 0  # 0=PremierLeague, 1=Superliga


# Strip data
df = data_strip(df, league, rounds, date_current)


# Get teams
teams = get_teams(league)


# Get data
db = get_data(df, teams, rounds, decimals)


# Print data    
print_data(db, rounds)

