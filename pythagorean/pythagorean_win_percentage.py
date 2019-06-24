import numpy as np
import matplotlib.pyplot as plt

def main():
  stats = get_all_stats()
  x, y = [], []
  for stat in stats:
    scored, allowed, wins = stat
    x.append(get_projected_wins(scored, allowed))
    y.append(wins)
  plt.scatter(x, y, s=5)
  line = np.arange(40, 120, .66)
  plt.plot(line, line, color='green')
  plt.title("Pythagorean Win Percentage")
  plt.xlabel("Projected")
  plt.ylabel("Observed")
  plt.show()

def get_projected_wins(runs_scored, runs_allowed):
  projected_percentage = (runs_scored**1.83) / (runs_scored**1.83 + runs_allowed**1.83)
  return 162 * projected_percentage

def get_all_stats():
  all_stats = []
  for season in list(range(1989, 2018)):
    stats = season_stats(season)
    for team in list(stats.keys()):
      scored, allowed, wins = stats[team]
      all_stats.append((scored, allowed, wins))
  return all_stats

'''
For the given season, returns a dictionary of every team with its corresponding [runs_scores, runs_allowed, wins]
'''
def season_stats(season):
  filename = '../season_stats/s' + str(season) + '.txt'
  team_stats = {}
  with open(filename) as season_file:
    for game_line in season_file:
      game_info = game_line.split(',')
      visiting_team = game_info[3][1:-1]
      home_team = game_info[6][1:-1]
      visiting_score = int(game_info[9])
      home_score = int(game_info[10])
      home_win = 1 if home_score > visiting_score else 0
      visiting_win = 1 if visiting_score > home_score else 0
      if home_team in list(team_stats.keys()):
        team_stats[home_team][0] += home_score 
        team_stats[home_team][1] += visiting_score
        team_stats[home_team][2] += home_win
      else:
        team_stats[home_team] = [home_score, visiting_score, home_win]
      if visiting_team in list(team_stats.keys()):
        team_stats[visiting_team][0] += visiting_score
        team_stats[visiting_team][1] += home_score
        team_stats[visiting_team][2] += visiting_win
      else:
        team_stats[visiting_team] = [visiting_score, home_score, visiting_win]
    season_file.close()
  return team_stats

main()

  