import pandas as pd

def scrape_schedule(date):
    schedule = pd.read_html("https://www.vegasinsider.com/college-basketball/scoreboard/scores.cfm/game_date/" + date)
    return schedule

schedule = scrape_schedule("02-22-2021")

for num, game in enumerate(schedule):
    if num >= 10 and num % 2 == 0:
        away_team_raw = game[0][2]
        if(away_team_raw[:1].isdigit()):
            away_team = away_team_raw.split(" ")[1]
        else:
            away_team = away_team_raw

        home_team_raw = game[0][3]
        if(home_team_raw[:1].isdigit()):
            home_team = home_team_raw.split(" ")[1]
        else:
            home_team = home_team_raw

        if str(game[1][2]) < "0":
            spread = float(game[1][2])
            over_under = float(game[1][3])
        else:
            spread = -1 * float(game[1][3])
            over_under = float(game[1][2])
    
        score_away = game[4][2]
        score_home = game[4][3]

        if not pd.isnull(spread) and not pd.isnull(score_home):      
            margin = int(score_home) - int(score_away)

            if margin > spread:
                home_result = 'W'
                away_result = 'L'
            elif margin < spread:
                home_result = 'L'
                away_result = 'W'
            elif margin == spread:
                home_result = 'P'
                away_result = 'P'
            else:
                home_result = 'NA'
                away_result = 'NA'

        if not pd.isnull(over_under) and not pd.isnull(score_home):

            total_score = int(score_home) + int(score_away)
            if total_score > over_under:
                over_under_result = 'OVER'
            elif total_score < over_under:
                over_under_result = 'UNDER'
            elif total_score == over_under:
                over_under_result = 'PUSH'
            else:
                over_under_result = 'NA'

        print(away_team + " " + str(spread) + " " + str(score_away) + " " + away_result)
        print(home_team + " " + str(over_under) + " " + str(score_home) + " " + home_result + " " + over_under_result)
        print("-----------------------------")