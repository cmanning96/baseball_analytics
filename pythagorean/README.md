**Pythagorean Win Percentage**

One of the most simple yet accurate predictors in baseball analytics is as follows:

In a season, a team's win percentage will be approximately equal to (Rs^2) / (Rs^2 + Ra^2), where Rs and Ra are how many runs the team scores and allows in that season. This equation is referred to as the pythagorean win percentage. (Note, the '^2' is usually replace with '^1.83')

Using gamelogs from the past 20 seasons, I plotted each team-season with the x-value being how many games the above equation predicted, and the y-value being the observed value of how many games they actually won.

![Resulting graph](https://github.com/cmanning96/baseball_analytics/blob/master/pythagorean/pythagorean_output.png?raw=true)