import pandas as pd
import seaborn as sns

teams = pd.read_csv("teams.csv")
teams = teams[["team", "country", "year", "athletes", "age", "prev_medals", "medals"]]

sns.lmplot(x="athletes", y="medals", data=teams, fit_reg=True, ci=None)

teams = team.dropna()

train = teams[teams[year] < 2012].copy()
test = teams[teams[year] >= 2012].copy()

train.shape()

