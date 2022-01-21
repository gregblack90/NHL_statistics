#
# Script to pull data from NHL API
#
# IMPORT STATEMENTS
import requests
import pandas as pd
import matplotlib.pyplot as plt
from ui import Ui_MainWindow


def GetSeasonData(self):
    # dictionary of teams
    team_dict = {"Anaheim Ducks": 24, "Arizona Coyotes": 53, "Boston Bruins": 6, "Buffalo Sabres": 7,
                 "Calgary Flames": 20, "Carolina Hurricanes": 12, "Chicago Blackhawks": 16, "Colorado Avalanche": 21,
                 "Columbus Blue Jackets": 29, "Dallas Stars": 25, "Detroit Red Wings": 17, "Edmonton Oilers": 22,
                 "Florida Panthers": 13, "Los Angeles Kings": 26, "Minnesota Wild": 30, "Montréal Canadiens": 8,
                 "Nashville Predators": 18, "New Jersey Devils": 1, "New York Islanders": 2, "New York Rangers": 3,
                 "Ottawa Senators": 9, "Philadelphia Flyers": 4, "Pittsburgh Penguins": 5, "San Jose Sharks": 28,
                 "Seattle Kraken": 55, "St. Louis Blues": 19, "Tampa Bay Lightning": 14, "Toronto Maple Leafs": 10,
                 "Vancouver Canucks": 23, "Vegas Golden Knights": 54, "Washington Capitals": 15, "Winnipeg Jets": 52}
    # get selected teams
    team_1 = self.team_1_select.currentText()
    team_2 = self.team_2_select.currentText()
    # get team ID needed for NHL API
    team_1_id = str(team_dict[team_1])
    team_2_id = str(team_dict[team_2])
    # get season stats for selected teams
    r1 = requests.get(url='https://statsapi.web.nhl.com/api/v1/teams/' + team_1_id + '/stats')
    r2 = requests.get(url='https://statsapi.web.nhl.com/api/v1/teams/' + team_2_id + '/stats')
    # convert response data into json
    json_data1 = r1.json()
    json_data2 = r2.json()
    # create dictionaries to store statistics
    record_stats_1 = {}
    record_stats_2 = {}
    # get team statistics (single season stats)
    #   RECORD
    gm_ply_1 = float(json_data1['stats'][0]['splits'][0]['stat']['gamesPlayed'])
    gm_ply_2 = float(json_data2['stats'][0]['splits'][0]['stat']['gamesPlayed'])
    wins_1 = float(json_data1['stats'][0]['splits'][0]['stat']['wins'])
    wins_2 = float(json_data2['stats'][0]['splits'][0]['stat']['wins'])
    loss_1 = float(json_data1['stats'][0]['splits'][0]['stat']['losses'])
    loss_2 = float(json_data2['stats'][0]['splits'][0]['stat']['losses'])
    ot_1 = float(json_data1['stats'][0]['splits'][0]['stat']['ot'])
    ot_2 = float(json_data2['stats'][0]['splits'][0]['stat']['ot'])
    pts_1 = float(json_data1['stats'][0]['splits'][0]['stat']['pts'])
    pts_2 = float(json_data2['stats'][0]['splits'][0]['stat']['pts'])
    pts_perc_1 = float(json_data1['stats'][0]['splits'][0]['stat']['ptPctg'])
    pts_perc_2 = float(json_data2['stats'][0]['splits'][0]['stat']['ptPctg'])
    # add keys and values to dictionary
    record_stats_1.update({'Games Played': gm_ply_1, 'Wins': wins_1, 'Losses': loss_1, 'OT': ot_1, 'Points': pts_1, 'Point %': pts_perc_1})
    record_stats_2.update({'Games Played': gm_ply_2, 'Wins': wins_2, 'Losses': loss_2, 'OT': ot_2, 'Points': pts_2, 'Point %': pts_perc_2})

    # get team statistics (single season stat rankings)
    wins_rnk_1 = json_data1['stats'][1]['splits'][0]['stat']['wins']
    wins_rnk_2 = json_data2['stats'][1]['splits'][0]['stat']['wins']

    # generate plots
    #   RECORD
    plt.bar(range(len(record_stats_1)), list(record_stats_1.values()), align='edge', width=0.2, label=team_1)
    plt.bar(range(len(record_stats_2)), list(record_stats_2.values()), align='edge', width=-0.2, label=team_2)
    plt.xticks(range(len(record_stats_1)), list(record_stats_1.keys()))
    plt.legend()
    plt.show()
