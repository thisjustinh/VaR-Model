# Futures

I need free historical data for futures! While I can easily get free stock options data from Yahoo Finance, other commodities are a lot harder to find.

## Yahoo Finance

Interestingly, Yahoo Finance also has information about commodities and derivatives pricing. So we use their data to help our pricing models.

One major problem, however, is the short range of data avaiable through Yahoo. Some of the data only contains the last 1.5 years of data, which isn't great for backtesting. But we do what we can.

### Futures Tickers

Quick rundown on what corresponds to what:

#### Agricultural Products

 - Corn: "C=F"
 - Oats: "O=F"
 - KC HRW Wheat Futures: "KW=F"
 - Rough Rice: "RR=F"
 - Soybean Meal: "SM=F"
 - Soybean Oil: "BO=F"
 - Soybeans: "S=F"
 - Feeder Cattle: "FC=F"
 - Lean Hogs: "LH=F"
 - Live Cattle: "LC=F"
 - Cocoa: "CC=F"
 - Coffee: "KC=F"
 - Cotton: "CT=F"
 - Lumber: "LB=F"
 - Orange Juice: "OJ=F"
 - Sugar #11: "SB=F"

#### Energy

 - Crude Oil: "CL=F"
 - Heating Oil: "HO=F"
 - Natural Gas: "NG=F"
 - RBOB Gasoline: "RB=F"
 - Brent Crude Oil: "BZ=F"

#### Metals

 - Gold: "GC=F"
 - Gold 100 oz: "ZG=F"
 - Silver: "SI=F"
 - Platinum: "PL=F"
 - Copper: "HG=F"
 - Palladium: "PA=F"

## Quandl

Using Quandl with their API for (hopefully free) data.

### Stevens Analytics Futures

Go [here](https://www.quandl.com/data/SRF-Reference-Futures) for free sample data for futures from 2014 to 2018.

### Community Wiki Continuous Futures

A very-cool collection of futures prices curated by the Quandl community. Completely free and open, but there are many different databases to sift through.

Check out the collection [here](https://www.quandl.com/data/CHRIS-Wiki-Continuous-Futures).

#### WTI Crude Oil

An example of a database from the above collection is this [link](https://www.quandl.com/data/CHRIS/ICE_T1-WTI-Crude-Futures-Continuous-Contract) to the WTI Crude Oil Futures.

### Foreign Exchanges

Quandl also have a lot of free data specific to certain exchanges in Asia, Europe, and even Canada, but nothing for America.

## Turtle Trader

No great API, but can import ZIP files with historical data. Go to the link [here](https://www.turtletrader.com/hpd/). Haven't looked at the data in detail yet.

## Bloomberg Terminal

If all else fails and you're not happy with the data that you've found, you can always fall back on exporting data from the Bloomberg Terminal through Excel. Unfortunately, having data locked behind proprietary software makes getting it much, much harder.
