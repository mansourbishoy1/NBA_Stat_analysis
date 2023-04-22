import time
import pandas as pd
from nba_api.stats.endpoints import playergamelog, Scoreboard, BoxScoreTraditionalV2
from nba_api.stats.static import players
from datetime import datetime, timedelta
today = datetime.now().strftime("%m/%d/%Y")

def get_todays_players(today):
    while True:
        try:
            scoreboard = Scoreboard(game_date=today)
            break
        except Exception as e:
            # Print the error message and wait before trying again
            print(f"straight: {str(e)}")
            time.sleep(1)

    # Get the list of games for today
    games = scoreboard.get_data_frames()[0]
    game_ids = games['GAME_ID']
    # Get the player IDs of players who are playing today
    player_ids = []
    for game_id in game_ids:
        boxscore = BoxScoreTraditionalV2(game_id=game_id)
        players = boxscore.player_stats.get_data_frame()
        player_ids_temp = players['PLAYER_ID'].tolist()
        player_ids = player_ids + player_ids_temp
    return player_ids
# Get the scoreboard for today's date




# Retrieve the player's game log for the regular season and playoffs
def get_df(player_id):
    while True:
        try:
            player_name = players.find_player_by_id(player_id)
            player_name = player_name['full_name']
            season_types = ['Regular Season', 'Playoffs']
            gamelogs = []
            for season_type in season_types:
                gamelog = playergamelog.PlayerGameLog(player_id=player_id, season='2022-23', season_type_all_star=season_type).get_data_frames()[0]
                gamelogs.append(gamelog)

            # Concatenate the DataFrames for regular season and playoffs
            combined_gamelog = pd.concat(gamelogs)

            # Select the columns we want to keep
            columns = ['GAME_DATE', 'MATCHUP', 'WL', 'PTS', 'REB', 'AST', 'STL', 'BLK', 'FG_PCT', 'FG3_PCT', 'FT_PCT']
            combined_gamelog = combined_gamelog[columns]
            combined_gamelog['GAME_DATE'] = pd.to_datetime(combined_gamelog['GAME_DATE'])

            # Sort the DataFrame by date
            combined_gamelog = combined_gamelog.sort_values('GAME_DATE', ascending=False)
            top30 = combined_gamelog.head(30)

            outdf = pd.DataFrame(columns = ['Name','5+ Points','10+ Points', '15+ Points','20+ Points','25+ Points','30+ Points','35+ Points','40+ Points','4+ Rebounds','6+ Rebounds','8+ Rebounds','10+ Rebounds','12+ Rebounds','14+ Rebounds','16+ Rebounds','2+ Assists','4+ Assists','6+ Assists','8+ Assists','10+ Assists','12+ Assists','14+ Assists'])
            outdf['Name'] = [player_name]
            # Calculating Points Percentages
            x = top30['PTS'].apply(lambda x: x >= 5)
            percent_5plus_pts = x.sum() / len(x) * 100 if len(x) != 0 else 0
            outdf['5+ Points'] = [percent_5plus_pts]
            x = top30['PTS'].apply(lambda x: x >= 10)
            percent_5plus_pts = x.sum() / len(x) * 100 if len(x) != 0 else 0
            outdf['10+ Points'] = [percent_5plus_pts]
            x = top30['PTS'].apply(lambda x: x >= 15)
            percent_5plus_pts = x.sum() / len(x) * 100 if len(x) != 0 else 0
            outdf['15+ Points'] = [percent_5plus_pts]
            x = top30['PTS'].apply(lambda x: x >= 20)
            percent_5plus_pts = x.sum() / len(x) * 100 if len(x) != 0 else 0
            outdf['20+ Points'] = [percent_5plus_pts]
            x = top30['PTS'].apply(lambda x: x >= 25)
            percent_5plus_pts = x.sum() / len(x) * 100 if len(x) != 0 else 0
            outdf['25+ Points'] = [percent_5plus_pts]
            x = top30['PTS'].apply(lambda x: x >= 30)
            percent_5plus_pts = x.sum() / len(x) * 100 if len(x) != 0 else 0
            outdf['30+ Points'] = [percent_5plus_pts]
            x = top30['PTS'].apply(lambda x: x >= 35)
            percent_5plus_pts = x.sum() / len(x) * 100 if len(x) != 0 else 0
            outdf['35+ Points'] = [percent_5plus_pts]
            x = top30['PTS'].apply(lambda x: x >= 40)
            percent_5plus_pts = x.sum() / len(x) * 100 if len(x) != 0 else 0
            outdf['40+ Points'] = [percent_5plus_pts]
            x = top30['REB'].apply(lambda x: x >= 4)
            percent_5plus_pts = x.sum() / len(x) * 100 if len(x) != 0 else 0
            # Calculating Rebound Percentages
            outdf['4+ Rebounds'] = [percent_5plus_pts]
            x = top30['REB'].apply(lambda x: x >= 6)
            percent_5plus_pts = x.sum() / len(x) * 100 if len(x) != 0 else 0
            outdf['6+ Rebounds'] = [percent_5plus_pts]
            x = top30['REB'].apply(lambda x: x >= 8)
            percent_5plus_pts = x.sum() / len(x) * 100 if len(x) != 0 else 0
            outdf['8+ Rebounds'] = [percent_5plus_pts]
            x = top30['REB'].apply(lambda x: x >= 10)
            percent_5plus_pts = x.sum() / len(x) * 100 if len(x) != 0 else 0
            outdf['10+ Rebounds'] = [percent_5plus_pts]
            x = top30['REB'].apply(lambda x: x >= 12)
            percent_5plus_pts = x.sum() / len(x) * 100 if len(x) != 0 else 0
            outdf['12+ Rebounds'] = [percent_5plus_pts]
            x = top30['REB'].apply(lambda x: x >= 14)
            percent_5plus_pts = x.sum() / len(x) * 100 if len(x) != 0 else 0
            outdf['14+ Rebounds'] = [percent_5plus_pts]
            x = top30['REB'].apply(lambda x: x >= 16)
            percent_5plus_pts = x.sum() / len(x) * 100 if len(x) != 0 else 0
            outdf['16+ Rebounds'] = [percent_5plus_pts]
            # Calculating Assists Percentages
            x = top30['AST'].apply(lambda x: x >= 2)
            percent_5plus_pts = x.sum() / len(x) * 100 if len(x) != 0 else 0
            outdf['2+ Assists'] = [percent_5plus_pts]
            x = top30['AST'].apply(lambda x: x >= 4)
            percent_5plus_pts = x.sum() / len(x) * 100 if len(x) != 0 else 0
            outdf['4+ Assists'] = [percent_5plus_pts]
            x = top30['AST'].apply(lambda x: x >= 6)
            percent_5plus_pts = x.sum() / len(x) * 100 if len(x) != 0 else 0
            outdf['6+ Assists'] = [percent_5plus_pts]
            x = top30['AST'].apply(lambda x: x >= 8)
            percent_5plus_pts = x.sum() / len(x) * 100 if len(x) != 0 else 0
            outdf['8+ Assists'] = [percent_5plus_pts]
            x = top30['AST'].apply(lambda x: x >= 10)
            percent_5plus_pts = x.sum() / len(x) * 100 if len(x) != 0 else 0
            outdf['10+ Assists'] = [percent_5plus_pts]
            x = top30['AST'].apply(lambda x: x >= 12)
            percent_5plus_pts = x.sum() / len(x) * 100 if len(x) != 0 else 0
            outdf['12+ Assists'] = [percent_5plus_pts]
            x = top30['AST'].apply(lambda x: x >= 14)
            percent_5plus_pts = x.sum() / len(x) * 100 if len(x) != 0 else 0
            outdf['14+ Assists'] = [percent_5plus_pts]
            return outdf
        except Exception as e:
            print(f"Error: {str(e)}")
            time.sleep(1)
player_ids = get_todays_players(today)
final_df = pd.DataFrame(columns = ['Name','5+ Points','10+ Points', '15+ Points','20+ Points','25+ Points','30+ Points','35+ Points','40+ Points','4+ Rebounds','6+ Rebounds','8+ Rebounds','10+ Rebounds','12+ Rebounds','14+ Rebounds','16+ Rebounds','2+ Assists','4+ Assists','6+ Assists','8+ Assists','10+ Assists','12+ Assists','14+ Assists'])
final_df.to_csv('mystats.csv', index=False)
count = 0
for player in player_ids:
    if(count<len(player_ids)):
        new_row = get_df(player)
        print(new_row)
        final_df.append(new_row)
        count+=1
        with open('mystats.csv', 'a', newline='') as f:
            new_row.iloc[-1:].to_csv(f, header=False, index=False)
    else:
        break
