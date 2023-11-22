

from flask import render_template, request

from src import app
from src.utilities import MasterProphet



@app.after_request
def add_header(response):
	response.headers["X-UA-Compatible"] = "IE=Edge,chrome=1"
	response.headers["Cache-Control"] = "public, max-age=0"
	return response

@app.route("/")
@app.route("/home")
def home():
	""" Renders the home page """
	return render_template(
		"index.html"
	)

@app.route("/predict", methods=["POST", "GET"])
def predict():
	ticker = request.form["ticker"]
	master_prophet = MasterProphet(ticker)

	forecast = master_prophet.forecast()

	actual_forecast = round(forecast.yhat[0], 2)
	lower_bound = round(forecast.yhat_lower[0], 2)
	upper_bound = round(forecast.yhat_upper[0], 2)
	bound = round(((upper_bound - actual_forecast) + (actual_forecast - lower_bound) / 2), 2)

	summary = master_prophet.info["summary"]
	country = master_prophet.info["country"]
	sector = master_prophet.info["sector"]
	website = master_prophet.info["website"]
	min_date = master_prophet.info["min_date"]
	max_date = master_prophet.info["max_date"]

	forecast_date = master_prophet.forecast_date.date()

	return render_template(
		"output.html",
		ticker = ticker.upper(),
		sector = sector,
		country = country,
		website = website,
		summary = summary,
		min_date = min_date,
		max_date = max_date,
		forecast_date = forecast_date,
		forecast = actual_forecast,
		bound = bound
		)
