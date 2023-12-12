import pandas as pd
import seaborn as sns
from sklearn.metrics import mean_absolute_error
from sklearn.linear_model import LinearRegression
import numpy as np
#import data and define necessary columns
teams = pd.read_csv("teams.csv")
teams = teams[["team", "country", "year", "athletes", "age", "prev_medals", "medals"]]

#plot data and remove rows with null values
sns.lmplot(x="athletes", y="medals", data=teams, fit_reg=True, ci=None)
teams = team.dropna()

#define test data to test predictions later
train = teams[teams[year] < 2012].copy()
test = teams[teams[year] >= 2012].copy()

#create linear regression model
reg = LinearRegression();
predictors= ["athletes", "prev_medals"]
target = "medals"
reg.fit(train[predictors], train["medals"])

predictions = reg.predict(test[predictors])

#any value less than zero is changed to zero
# and all values are rounded to nearest whole num
test.loc[test["predictions"] < 0, "predictions"] = 0
test["predictions"] = test["predictions"].round()

#calculate errors
error = mean_absolute_error(test["medals"], test["predictions"])

teams.describe()["medals"]

test[test["team"] == "USA"]

errors = (test["medals"] - test["predictions"]).abs()
error_by_team = errors.groupby(test["team"]).mean()
medals_by_team = test["medals"].groupby(test["team"]).mean()

error_ratio = error_by_team / medals_by_team
error_ratio = error_ratio[np.isfinite(error_ratio)]

