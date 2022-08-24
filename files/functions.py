import pandas as pd
import numpy as np
import datetime as dt
import csv


def data_strip(df, league, rounds, date_current):
    
    if league == 0: 
        df = df[df['league'] == 'Barclays Premier League']
    elif league == 1:
        df = df[df['league'] == 'Danish SAS-Ligaen']


    # Convert date into datetime
    old_dates = df['date'].unique()

    for od in old_dates:
        text = od.split('-')
        date = dt.datetime(int(text[0]), int(text[1]), int(text[2]))
        df = df.replace(od, date)

    # Remove previous rounds
    df = df[df['date'] > date_current]
    
    return df



def get_data(df, teams, rounds, decimals):
    header = ["Round", "1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17"]
    db = []

    print("%4s" % "Team", end ="   ")
    for i in range(rounds):
        print("%-4d" % (i+1), end ="   ")
    print("%-4s" % "avg") 
        
    with open('./data.csv', 'w', encoding='UTF8', newline='') as f:
        
        writer = csv.writer(f)
        writer.writerow(header)

        for team in teams:
            odds = [team.arc]
            opps = []
            data = [team.arc]
            
            df2 = df
            df2 = df2[(df2['team1'] == team.name) | (df['team2'] == team.name)]
            
            # Relevant games after start-date
            df2 = df2[0:rounds]
            
            for i in range(rounds):    
                if df2.iloc[i]['team1'] == team.name:
                    odds.append(df2.iloc[i]['prob1'])
                    data.append(str(df2.iloc[i]['prob1']).replace('.',','))
                    opps.append(df2.iloc[i]['team2'])
                else:
                    odds.append(df2.iloc[i]['prob2'])
                    data.append(str(df2.iloc[i]['prob2']).replace('.',','))
                    opps.append(df2.iloc[i]['team1'])
            
            writer.writerow(data)
            odds.append( round(np.mean(odds[1:]) * decimals) / decimals )
            
            db.append(odds)
        
        f.close()
        
    return db



def print_data(db, rounds):
    db.sort(key=lambda row: (row[-1]), reverse=True)

    for item in db:
        print("%-4s" % item[0], end ="   ")
        for i in range(rounds):
            print("%-0.2f" % item[i+1], end ="   ")
        print("%-0.2f" % item[-1]) 
