from quantlib import var

import click
from datetime import datetime
from dateutil.relativedelta import relativedelta

@click.command()
@click.option("--ticker", "-t", "ticker", required=True, help="Specify ticker")
@click.option("--start-date", "-s", "start", default=datetime.now() - relativedelta(years=1))
@click.option("--end-date", "-e", "end", default=datetime.now())
@click.option("--confidence", "-c", "conf", required=True, help="Confidence level for VaR (usually .95 or .99)") 
@click.option("--method", "-m", "method", default="variance-covariance")
@click.option("--days", "-d", "days", default=30)
@click.option("--trials", "-tr", "trials", default=1000)
def get_var(ticker, start, end, conf, method, days, trials):
    if method == "variance-covariance":
        return var.variance_var(ticker, start, end, conf)
    elif method == "historical":
        return var.historical_var(ticker, start, end, conf)
    elif method == "monte-carlo":
        return var.mc_var(ticker, start, end, conf, days, trials)
    else:
        raise ValueError("Method must be 'variance-covariance', 'historical', or 'monte-carlo'")


if __name__ == '__main__':
    get_var()

