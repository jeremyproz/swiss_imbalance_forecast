# Documentation
The structure presents a modular repo that is executed regularly in a batch and can be tested independently. Constants are stored in a yaml in the configs directory. Source code includes several jobs which are explained further below. 

The main package imbalance_forecast executes all jobs from __main__.py and first calls functions from utils to retrieve constants from the yaml file.

## Data scraping
This job scrapes data from various endpoints to update a database hosted by cloudflare R2 services. It allows for rolling updates or complete rewrites. It also provides various functions to retrieves and update data from said database.

## Forecast
This job creates multiple forecasts for the imbalance price in Switzerland. It then stores the forecast in the database either incrementally or in a batch. In the present version, this includes:
- chronos 2 - a 120M parameter fundamental model, used to zero shot forecast the forecast

## Evalutation
This job evaluates forecasts according to several common metrics and stores this information in the database.