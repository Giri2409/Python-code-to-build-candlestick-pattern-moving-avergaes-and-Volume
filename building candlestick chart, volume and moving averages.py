# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 12:10:19 2023

@author: bopg001
"""

!pip install mplfinance

import yfinance as yf
import mplfinance as mpf

from datetime import datetime, time

start = datetime.now()
end=start.replace(year=start.year-1)

data=yf.download("TSLA",end,start)

#building candlestick chart, moving average and volume

mpf.plot(data, type="candle", mav=(7,14,21), volume=True)



