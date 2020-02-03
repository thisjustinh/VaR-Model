import yfinance as yf
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import norm

DEBUG = True


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


def getValueAtRisk(ticker: str, start: str, end: str, conf: float):
    """
    Calculates Value at Risk (VaR) for a cer+
    tain equity
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
    return mu - ppf*sigma   # Subtract average returns from the maximum expected loss (ppf * standard deviation)


def simulateValueAtRisk(ticker: str, start: str, end: str, conf: float, days: int, trials: int):
    """
    Calculate Value at Risk (VaR) using Monte-Carlo Simulation
    """
    historical_eod = yf.Ticker(ticker).history(start=start, end=end)
    returns = np.log(1 + historical_eod['Close'].pct_change())

    mu = returns.mean()
    drift = mu - (0.5 * returns.var())
    sigma = returns.std()
    
    predicted_returns = np.exp(drift + sigma + norm.ppf(np.random.rand(days, trials)))
    
    return_list = np.zeros_like(predicted_returns)
    return_list[0] = historical_eod['Close'].iloc[-1]
    for t in range(1, days):
        return_list[t] = return_list[t - 1] * predicted_returns[t]
    
    # plt.figure(figsize=(10, 6))
    plt.plot(return_list)
    plt.show()

    return_list = np.sort(return_list[-1])
    return (return_list[int((1 - conf) * trials)] - historical_eod['Close'].iloc[-1]) / historical_eod['Close'].iloc[-1]



if __name__=='__main__' and DEBUG:
    # ticker = input("Enter ticker: ")
    # start = input("Enter data start date (YYYY-MM-DD): ")
    # end = input("Enter data end date (YYYY-MM-DD): ")
    # conf = input("Enter confidence level (.95 or .99): ")
    # print(f"Value at Risk (VaR) at {conf} confidence is {getValueAtRisk(ticker, start, end, float(conf))}")
    
    print(simulateValueAtRisk("aapl", "2020-01-01", "2020-02-03", .95, 30, 1000))
