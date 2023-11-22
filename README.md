# Warren - Stock Price Predictor

Stock market prediction is the act of trying to determine the future value of a company stock or other financial instrument traded on an exchange. The successful prediction of a stock's future price could yield significant profit. The efficient-market hypothesis suggests that stock prices reflect all currently available information and any price changes that are not based on newly revealed information thus are inherently unpredictable. Others disagree and those with this viewpoint possess myriad methods and technologies which purportedly allow them to gain future price information.

We make use of Facebook's Time Series forcasting algorithm Prophet to predict stock market price of US based companies in real time using multi-variate, single step forecasting strategy.

![Header](src/static/images/main_page.png)

## Getting Started

Download or clone project from github:
```
$ git clone https://github.com/nityansuman/warren.git
```

Create a project environment (Anaconda recommended):
```
$ conda create --name envname python
$ conda activate envname
```

Install prerequisites:
```
$ pip install -r REQUIREMENTS.txt
```

Run project:
```
$ cd warren
$ python runserver.py
```

## Model Validation Analysis

**Facebook (Stock: FB) Validation**
![FB_validation](src/static/images/fb_forecast_30_day_validation.png)

**Microsoft (Stock: MSFT) Validation**
![MSFT_validation](src/static/images/msft_forecast_30day_validation.png)

**Google (Stock: GOOGL) Validation**
![GOOGLE_validation](src/static/images/googl_forecast_30day_validation.png)

## Support

If you like the work I do, show your appreciation by 'FORK', 'STAR' and 'SHARE'.

[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)
[![Forthebadge](https://forthebadge.com/images/badges/built-with-love.svg)](https://forthebadge.com)
# Stock-Market-Predictor-using-Prophet
