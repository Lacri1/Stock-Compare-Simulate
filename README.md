# stock-compare-and-simulate

A simple toolkit for comparing, simulating, and generating stock price data.


## Files

- `plot_normalized_comparison.py`  
  Compare two real stock normalized percentage plots.

- `plot_base_theoretical_3x.py`  
  Simulate a theoretical 3x leveraged version of a base asset and plot it.

- `Stock_Price_Generator.js`  
  Randomly generates one year of daily stock prices, with adjustable volatility.

  ## Data

> ⚠️ **Note:** This repository does not include any real price data.  
> Please provide your own stock price data files or use an API (like `yfinance`) to load them.

You can also easily fetch market data using the `get_market_trend` function  
from the [MCP](https://github.com/Lacri1/MCP).  
It provides convenient access to historical stock and ETF prices in a ready-to-use format.


```bash
python plot_normalized_comparison.py
python plot_base_theoretical_3x.py
node Stock_Price_Generator.js
