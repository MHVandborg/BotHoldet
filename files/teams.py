from files.classes import *

def get_teams(league):
    teams = []
    
    if league == 0:
        teams = [Team('Arsenal', 'ARS'),
                 Team('Aston Villa', 'AVI'),
                 Team('AFC Bournemouth', 'BOU'),
                 Team('Brentford', 'BRE'),
                 Team('Brighton and Hove Albion', 'BRI'),
                 Team('Chelsea', 'CHE'),
                 Team('Crystal Palace', 'CP '),
                 Team('Everton', 'EVE'),
                 Team('Fulham', 'FUL'),
                 Team('Leeds United', 'LEE'),
                 Team('Leicester City', 'LEI'),
                 Team('Liverpool', 'LIV'),
                 Team('Manchester City', 'MAC'),
                 Team('Manchester United', 'MAU'),
                 Team('Newcastle', 'NEW'),
                 Team('Nottingham Forest', 'NFO'),
                 Team('Southampton', 'SOU'),
                 Team('Tottenham Hotspur', 'TOT'),
                 Team('West Ham United', 'WHA'),
                 Team('Wolverhampton', 'WOL')]
    elif league == 1:
        teams = [Team('AC Horsens', 'ACH'),
                 Team('AGF Aarhus', 'AGF'),
                 Team('Brondby', 'BIF'),
                 Team('AaB', 'AAB'),
                 Team('Lyngby', 'LBK'),
                 Team('Viborg', 'VFF'),
                 Team('FC Midtjylland', 'FCM'),
                 Team('Silkeborg', 'SIF'),
                 Team('Odense BK', 'OB '),
                 Team('Randers FC', 'RFC'),
                 Team('FC Copenhagen', 'FCK'),
                 Team('FC Nordsjaelland', 'FCN')]
    
    return teams