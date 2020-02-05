import yfinance as yf
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import norm


DEBUG = False


def portfolioValueAtRisk(portfolio: dict, start: str, end: str, conf: float):
    """
    Calculates overall Value at Risk (VaR) for a portfolio of equities.
    @param portfolio: Dictionary of equities, where the key is the ticker and value is its weight in the portfolio (% dollar value)
    @param start: Start date for eod-values
    @param end: End date for eod-values
    @param conf: Confidence level (either .95 or .99, usually)
    """

    values = []
    for ticker, weight in portfolio:
        values.append(weight * getValueAtRisk(ticker, start, end, conf))
    return sum(values)

def historicalValueAtRisk(ticker: str, start: str, end: str, conf: float):
    """
    Calculates Value at Risk (VaR) for a certain equity by checking historical returns
    """
    # Get historical eod values and calculate percent returns per day
    historical_eod = yf.Ticker(ticker).history(start=start, end=end)
    returns = historical_eod['Close'].pct_change()

    returns = np.sort(returns)
    return round(returns[int((1 - conf) * returns.size)], 4)

def getValueAtRisk(ticker: str, start: str, end: str, conf: float):
    """
    Calculates Value at Risk (VaR) for a certain equity
    @param ticker: Equity ticker
    @param start: Start date for eod-values
    @param end: End date for eod-values
    @param conf: Confidence level (either .95 or .99, usually)
    """
    
    # Get historical eod values and calculate percent returns per day.
    historical_eod = yf.Ticker(ticker).history(start=start, end=end)
    returns = historical_eod['Close'].pct_change()

    # Calculate expected value, standard deviation from historical data
    mu = returns.mean()
    sigma = returns.std()  # TODO: use unbiased estimator (n-1) or not?
    ppf = norm.ppf(1 - conf)  # Get ppf of normal distribution at inverse of confidence level
    return round(mu + ppf*sigma, 4)   # Subtract average returns from the maximum expected loss (ppf * standard deviation)


def simulateValueAtRisk(ticker: str, start: str, end: str, conf: float, days: int, trials: int):
    """
    Calculate Value at Risk (VaR) using Monte-Carlo Simulation
    """
    historical_eod = yf.Ticker(ticker).history(start=start, end=end)
    returns = historical_eod['Close'].pct_change()
    ln_returns = np.log(1 + returns)
    
    mu = np.array(ln_returns.mean())
    drift = np.array(mu - 0.5 * ln_returns.var())
    sigma = np.array(ln_returns.std())

    mc_returns = np.exp(drift + sigma * norm.ppf(np.random.rand(days, trials)))

    prices = np.zeros_like(mc_returns)
    prices[0] = historical_eod['Close'].iloc[-1]
    for day in range(1, days):
        prices[day] = prices[day - 1] * mc_returns[day]

    if DEBUG:
        print(mu, drift, sigma)
        print(mc_returns)
        print(prices)

    plt.plot(prices)
    plt.show()

    # Get maximum possible loss at confidence level
    last_price = prices[-1]
    mc_change = (last_price - np.array(historical_eod['Close'].iloc[-1])) / np.array(historical_eod['Close'].iloc[-1])

    if DEBUG:
        print(mu, drift, sigma)
        print(mc_returns)
        print(prices)
        print(mc_change)

    return np.sort(mc_change)[int((1 - conf) * trials)]


if __name__=='__main__':
    ticker = input("Enter ticker: ")
    start = input("Enter data start date (YYYY-MM-DD): ")
    end = input("Enter data end date (YYYY-MM-DD): ")
    conf = input("Enter confidence level (.95 or .99): ")
    print(f"Value at Risk (VaR) at {conf} confidence is historically {historicalValueAtRisk(ticker, start, end, float(conf))} and variance-covariance {getValueAtRisk(ticker, start, end, float(conf))}")
    
    print(f"One-month projection for VaR with Monte-Carlo is {simulateValueAtRisk(ticker, start, end, float(conf), 30, 1000)}.")
