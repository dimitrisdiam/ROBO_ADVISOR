# ROBO_ADVISOR
### PLEASE, WAIT UNTIL THE CHARTS TO SEE THE PROCESS COMPLETED.
![ezgif com-gif-maker](https://user-images.githubusercontent.com/64299794/165606538-087f3709-a0c9-4e01-8bdb-9191d021280e.gif)

# THEME
A robo-advisor works by first gathering information on a client through an online survey and then automatically suggests the appropriate portfolio investment for the client based on that data. 

* The risk allocation strategy, as well as the sectors selection, are based on sophisticated financial technics created for a target group of Luxembourgish adults between 20 and 30 years old.

# yahoof.py

### FEATURES

It's the most important file about this project. Based on the yfinance library I managed to get the final costs of different ETFs for a specific long or short period. 

ETFs: It's every key in FIX_TOKEN.

CRYPTOS: It's every key in FIX_CRYPTO.

ESG: It's every key in FIX_ESG.

PORTFOLIO: It's every column that are created by the values of FIX_TOKEN.

* Add or remove as ETFs, CRYPTOS or ESG as want.



### The algorithm provides many data like:

token_dict: Returns a dictionary with the names and all closing prices for every ETF in FIX_TOKEN, FIX_CRYPTO, and FIX_ESG in the specific period (FROM_DAY & TO_DAY).

zero_token_dict: Returns a dictionary with the names and all closing prices, WHICH WERE MODIFIED TO BECOME EASILY COMPARABLE TO EACH OTHER, for every ETF in FIX_TOKEN in the specific period (FROM_DAY & TO_DAY).

zero_cryptos_dict: Returns a dictionary with the names and all closing prices, WHICH WERE MODIFIED TO BECOME EASILY COMPARABLE TO EACH OTHER, for every CRYPTO in FIX_CRYPTO in the specific period (FROM_DAY & TO_DAY).

zero_esg_dict: Returns a dictionary with the names and all closing prices, WHICH WERE MODIFIED TO BECOME EASILY COMPARABLE TO EACH OTHER, for every ESG in FIX_ESG in the specific period (FROM_DAY & TO_DAY).

risk_profile_dict: Returns a double dictionary with the number of each portfolio as key and all ETFs, CRYPTOS and ESG as a second key with fixed percentages of FIX_TOKEN as values.

portfolio_dict: Returns a dictionary with the values of every suggested Portfolio (The process is out of coding, it is just mathematics).

performance_of_each_portfolio: Returns a list with the ratio of the progress of each suggested Portfolio during the specific period.
