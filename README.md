# ROBO_ADVISOR
![ezgif com-gif-maker](https://user-images.githubusercontent.com/64299794/165606538-087f3709-a0c9-4e01-8bdb-9191d021280e.gif)

# THEME
A robo-advisor works by first gathering information on a client through an online survey and then automatically suggests the appropriate portfolio investment for the client based on that data. 

* The risk allocation strategy, as well as the sectors selection, are based on sophisticated financial technics created for a target group of Luxembourgish adults between 20 and 30 years old.

# yahoof.py
It's the most important file about the project. Based on the yfinance library I managed to get the final costs of different ETFs for a specific long or short period. The algorithm provides many data like:

self.token_dict: returns a dictionary with the names and all closing prices for every ETF in FIX_TOKEN, FIX_CRYPTO, and FIX_ESG in the specific period ( FROM_DAY & TO_DAY)
