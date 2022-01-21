#
# This file contains code to setup the GUI UI
#
import datetime


class UiSetup:
    def compare_teams_ui(self):
        # - add teams to dropdowns
        teams = ["Anaheim Ducks", "Arizona Coyotes", "Boston Bruins", "Buffalo Sabres", "Calgary Flames",
                 "Carolina Hurricanes", "Chicago Blackhawks", "Colorado Avalanche", "Columbus Blue Jackets",
                 "Dallas Stars", "Detroit Red Wings", "Edmonton Oilers", "Florida Panthers", "Los Angeles Kings",
                 "Minnesota Wild", "Montréal Canadiens", "Nashville Predators", "New Jersey Devils",
                 "New York Islanders", "New York Rangers", "Ottawa Senators", "Philadelphia Flyers",
                 "Pittsburgh Penguins", "San Jose Sharks", "Seattle Kraken", "St. Louis Blues", "Tampa Bay Lightning",
                 "Toronto Maple Leafs", "Vancouver Canucks", "Vegas Golden Knights", "Washington Capitals",
                 "Winnipeg Jets"]
        self.team_1_select.addItems(teams)
        self.team_2_select.addItems(teams)
        #   - get current season to display to user
        cur_month = datetime.datetime.now().month
        cur_year = datetime.datetime.now().year
        disp_season = ""
        #   - formatting depends on where teams are on in season
        #   - if the new year hasn't occurred during the season yet,
        #       beginning year of season is current year, ending year of season is next year
        if 10 <= cur_month <= 12:
            beg_season_str = str(cur_year)
            end_season = cur_year + 1
            end_season_str = str(end_season)
            disp_season = beg_season_str + "-" + end_season_str[2:]
        #   - if the new year has occurred during the season,
        #       beginning year of season is year prior, ending year of season is current year
        elif 1 <= cur_month <= 6:
            beg_season = cur_year - 1
            beg_season_str = str(beg_season)
            end_season_str = str(cur_year)
            disp_season = beg_season_str + "-" + end_season_str[2:]
        # update label
        self.display_current_season.setText(disp_season)
