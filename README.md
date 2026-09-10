# swiss_imbalance_forecast
A simple forecast of the total system imbalance on the Swiss power grid.

## The Background
TLDR: big power plants can now sell/buy more than they planned and make big money.

In 2026, Swissgrid introduced a new imbalance pricing mechanism which allows asset owners to profit from imbalances on the whole Swiss power grid, thus following many other EU power grid markets. This has opened up new revenue streams for asset owners who previously made profit from the spot markets or the ancillary services markets. In the best case scenario, they would predict system imbalance and change their positions actively although this demands a certain affinity to forecasting and how the system works and not every asset owner does so.

## The goal
Show off how easily asset owners can help the power system and get paid in a clean, public repo.
- automatic, once per day forecast for the whole next day (more granularity maybe in a future update)
- model performance metrics
- automatically updated database
- a simple interface to retrain the model with the newest data
- a simple interface to rebuild the database from scratch

## The target audience
Battery operators, small powerplant operators or anyone participating in the Swiss wholesale markets. Use it to forecast your own revenues by cross-referencing this to the intraday price if you had traded products there using this forecast.