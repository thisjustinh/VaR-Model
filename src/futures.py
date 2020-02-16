import yfinance as yf
import pandas as pd
import numpy as np

crude_oil = yf.Ticker("CL=F")
hist = crude_oil.history()
print(hist.head())
print(crude_oil.info)
