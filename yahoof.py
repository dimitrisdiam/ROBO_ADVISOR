import yfinance as yf
import datetime
from datetime import datetime
from datetime import date


FIX_TOKEN = {
          #   1       2      3       4       5      "BITO"   ESG 1   ESG 2    ESG 3    ESG 4   ESG 5     PORTFOLIOS
    "IVV": [0.12,   0.144,  0.18,   0.204,   0.24,  0.216,  0.048,  0.0576,  0.072,   0.0816,  0.096],  # The first has to be FULL.
    "VHT": [0.09,   0.108,  0.135,  0.153,   0.18,  0.162,  0.036,  0.0432,  0.054,   0.0612,  0.072],
    "BOTZ": [0.03,  0.036,  0.045,  0.051,   0.06,  0.054,  0.012,  0.0144,  0.018,   0.0204,  0.024],
    "SPEU": [0.06,  0.072,  0.09,   0.102,   0.12,  0.108,  0.024,  0.0288,  0.036,   0.0408,  0.048],
    "VGT": [0.10,   0.12,   0.15,   0.17,    0.20,  0.18,   0.04,   0.048,   0.06,    0.068,   0.08],
    "VWO": [0.10,   0.12,   0.15,   0.17,    0.20,  0.18,   0.04,   0.048,   0.06,    0.068,   0.08],
    "GBIL": [0.075, 0.06,   0.0375, 0.0225,  0.00,  0.00,   0.03,   0.024,   0.015,   0.009,   0.00],
    "JPST": [0.075, 0.06,   0.0375, 0.0225,  0.00,  0.00,   0.03,   0.024,   0.015,   0.009,   0.00],
    "VTIP": [0.075, 0.06,   0.0375, 0.0225,  0.00,  0.00,   0.03,   0.024,   0.015,   0.009,   0.00],
    "MUB": [0.075,  0.06,   0.0375, 0.0225,  0.00,  0.00,   0.03,   0.024,   0.015,   0.009,   0.00],
    "AGG": [0.075,  0.06,   0.0375, 0.0225,  0.00,  0.00,   0.03,   0.024,   0.015,   0.009,   0.00],
    "BNDX": [0.075, 0.06,   0.0375, 0.0225,  0.00,  0.00,   0.03,   0.024,   0.015,   0.009,   0.00],
    "EMB": [0.05,   0.04,   0.025,  0.015,   0.00,  0.00,   0.02,   0.0160,  0.01,    0.006,   0.00],
}

FIRST_TOKEN = FIX_TOKEN["IVV"]


FIX_CRYPTO = {
           #   1     2     3     4     5  "BITO" ESG 1 ESG 2 ESG 3 ESG 4 ESG 5 PORTFOLIOS
    "BITO": [0.00, 0.00, 0.00, 0.00, 0.00, 0.10, 0.00, 0.00, 0.00, 0.00, 0.00],
}

FIX_ESG = {
            #   1          2     3     4     5  "BITO" ESG 1 ESG 2 ESG 3 ESG 4 ESG 5 PORTFOLIOS
    "ICLN": [0.00,       0.00, 0.00, 0.00, 0.00, 0.00, 0.15, 0.18, 0.23, 0.26, 0.30],
    "ESGV": [0.00,       0.00, 0.00, 0.00, 0.00, 0.00, 0.15, 0.18, 0.23, 0.26, 0.30],
    "FLOT": [0.00,       0.00, 0.00, 0.00, 0.00, 0.00, 0.30, 0.24, 0.15, 0.09, 0.00],
}

SECTORS = {
          # Technology       Healthcare       Industrials     Financial Services   Consumer Cyclical      Rest
    "IVV": [0.2552,            0.1367,           0.0813,         0.1319,             0.1181,             0.2768],
    "VHT": [0.0002,            0.9931,           0.0002,         0.0003,             0.0002,             0.0060],
    "BOTZ": [0.3998,           0.1594,           0.3789,         0.0448,             0.0112,             0.0059],
    "SPEU": [0.0746,           0.1454,           0.1502,         0.1580,             0.0951,             0.3767],
    "VGT": [0.9126,            0.0006,           0.0151,         0.0666,             0.0003,             0.0048],
    "VWO": [0.1778,            0.0426,           0.0657,         0.2019,             0.1218,             0.3902],
    "GBIL": [0.0,              0.0,              0.0,            0.0,                0.0,                0.0],
    "JPST": [0.0,              0.0,              0.0,            0.0,                0.0,                0.0],
    "VTIP": [0.0,              0.0,              0.0,            0.0,                0.0,                0.0],
    "MUB": [0.0,               0.0,              0.0,            0.0,                0.0,                0.0],
    "AGG": [0.0,               0.0,              0.0,            0.0,                0.0,                0.0],
    "BNDX": [0.0,              0.0,              0.0,            0.0,                0.0,                0.0],
    "EMB": [0.0,               0.0,              0.0,            0.0,                0.0,                0.0],
    "BITO": [0.0,              0.0,              0.0,            0.0,                0.0,                0.0],
    "ICLN": [0.0,              0.0,              0.0,            0.0,                0.0,                0.0],
    "ESGV": [0.0,              0.0,              0.0,            0.0,                0.0,                0.0],
    "FLOT": [0.0,              0.0,              0.0,            0.0,                0.0,                0.0],
}

FIELDS = ["Technology", "Healthcare", "Industrials", "Financial Services", "Consumer Cyclical", "Rest"]


NUMBER_OF_SUGGESTIONS_PORTFOLIOS = 5
FROM_DAY = "2019-01-02"
TO_DAY = date.today()


class FinanceY:

    def __init__(self):

        self.number_of_suggestions_portfolios = NUMBER_OF_SUGGESTIONS_PORTFOLIOS
        self.token_dict = {}
        self.zero_token_dict = {}
        self.zero_cryptos_dict = {}
        self.zero_esg_dict = {}
        self.risk_profile_dict = {}
        self.portfolio_dict = {}
        self.recorded_days = []
        self.exist_of_crypto = False
        self.exist_of_esg = False
        self.FIX_TOKEN = FIX_TOKEN
        self.FIX_CRYPTO = FIX_CRYPTO
        self.FIX_ESG = FIX_ESG
        self.SECTORS = SECTORS
        self.percentage_pies = {}
        self.performance_of_each_portfolio = []

        self.TOKEN = []
        self.CRYPTOS = []
        self.ESG = []

        for token in FIX_TOKEN:
            self.TOKEN.append(token)

        for crypto in FIX_CRYPTO:
            self.CRYPTOS.append(crypto)

        for esg in FIX_ESG:
            self.ESG.append(esg)

        if len(self.CRYPTOS) > 0:
            self.exist_of_crypto = True

        if len(self.ESG) > 0:
            self.exist_of_esg = True

        # CREATE A LIST WITH THE RECORDED DAYS.
        df = yf.download(self.TOKEN[0], start=FROM_DAY, end=TO_DAY, group_by="ticker")
        list_of_dataframe_by_yahoo = df.index
        for day in list_of_dataframe_by_yahoo:
            modified_day_to_sting = day.strftime('%Y-%m-%d')
            self.recorded_days.append(datetime.strptime(modified_day_to_sting, '%Y-%m-%d'))

        # CREATE THE RAW TOKEN LIST.
        for token in self.TOKEN:
            df = yf.download(token, start=FROM_DAY, end=TO_DAY, group_by="ticker")
            self.token_dict[token] = []
            for value in df["Adj Close"]:
                self.token_dict[token].append(float(value))

            # CREATE THE ZERO LIST.
            self.zero_token_dict[token] = []
            self.zero_token_dict[token].append(100)
            for value in range(1, len(self.token_dict[token])):
                new_value = (((self.token_dict[token][value] - self.token_dict[token][value - 1]) / self.token_dict[token][value - 1]) + 1) * self.zero_token_dict[token][value - 1]
                self.zero_token_dict[token].append(new_value)

        # CREATE THE RAW CRYPTOS LIST.
        for crypto in self.CRYPTOS:
            df = yf.download(crypto, start=FROM_DAY, end=TO_DAY, group_by="ticker")
            self.token_dict[crypto] = []
            for value in df["Adj Close"]:
                self.token_dict[crypto].append(float(value))

            # CREATE THE ZERO LIST.
            self.zero_cryptos_dict[crypto] = []
            self.zero_cryptos_dict[crypto].append(100)
            for value in range(1, len(self.token_dict[crypto])):
                new_value = (((self.token_dict[crypto][value] - self.token_dict[crypto][value - 1]) / self.token_dict[crypto][value - 1]) + 1) * self.zero_cryptos_dict[crypto][value - 1]
                self.zero_cryptos_dict[crypto].append(new_value)

        # CREATE THE RAW ESG LIST.
        for esg in self.ESG:
            df = yf.download(esg, start=FROM_DAY, end=TO_DAY, group_by="ticker")
            self.token_dict[esg] = []
            for value in df["Adj Close"]:
                self.token_dict[esg].append(float(value))

            # CREATE THE ZERO LIST.
            self.zero_esg_dict[esg] = []
            self.zero_esg_dict[esg].append(100)
            for value in range(1, len(self.token_dict[esg])):
                new_value = (((self.token_dict[esg][value] - self.token_dict[esg][value - 1]) / self.token_dict[esg][value - 1]) + 1) * self.zero_esg_dict[esg][value - 1]
                self.zero_esg_dict[esg].append(new_value)

        # FILL THE GAPS. ECT. FOR CRYPTO THAT HAS GAP YEAR.
        for crypto in self.CRYPTOS:
            while len(self.zero_cryptos_dict[crypto]) < len(self.recorded_days):
                self.zero_cryptos_dict[crypto].insert(0, 0)

        # CREATE PERCENTAGE DICTIONARY. ---->   {0: {'VTI': 0.2, 'VTV': 0.23, 'VOE': 0.12}}
        for portfolio in range(0, len(FIRST_TOKEN)):
            self.risk_profile_dict[portfolio] = {}
            for token in FIX_TOKEN:
                self.risk_profile_dict[portfolio][token] = FIX_TOKEN[token][portfolio]
            for crypto_token in self.CRYPTOS:
                self.risk_profile_dict[portfolio][crypto_token] = FIX_CRYPTO[crypto_token][portfolio]
            for esg_token in self.ESG:
                self.risk_profile_dict[portfolio][esg_token] = FIX_ESG[esg_token][portfolio]

        # CREATE THE TOKEN PORTFOLIO.
        for suggest in range(0, len(FIRST_TOKEN)):
            self.portfolio_dict[suggest] = []
            self.portfolio_dict[suggest].append(100)

            for tries in range(1, len(self.recorded_days)):
                total = 0
                for token_text in self.TOKEN:
                    new = self.zero_token_dict[token_text][tries] * self.risk_profile_dict[suggest][token_text]
                    total += new
                for crypto_text in self.CRYPTOS:
                    new = self.zero_cryptos_dict[crypto_text][tries] * self.risk_profile_dict[suggest][crypto_text]
                    total += new
                for esg in self.ESG:
                    new = self.zero_esg_dict[esg][tries] * self.risk_profile_dict[suggest][esg]
                    total += new

                self.portfolio_dict[suggest].append(total)

        self.short_list = [0.15, 0.12, 0.075, 0.045, 0.0, 0.0, 0.06, 0.048, 0.03, 0.018, 0.0]
        self.long_list = [0.35, 0.28, 0.175, 0.105, 0.0, 0.0, 0.14, 0.112, 0.07, 0.042, 0.0]
        self.esg_list = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.6, 0.6, 0.6, 0.6, 0.6]
        self.crypto_list = [0.0, 0.0, 0.0, 0.0, 0.0, 0.1, 0.0, 0.0, 0.0, 0.0, 0.0]

        for suggest in range(0, len(FIRST_TOKEN)):
            self.percentage_pies[suggest] = {}
            self.percentage_pies[suggest]["Short"] = self.short_list[suggest]
            self.percentage_pies[suggest]["Long"] = self.long_list[suggest]
            self.percentage_pies[suggest]["ESG"] = self.esg_list[suggest]
            self.percentage_pies[suggest]["Crypto"] = self.crypto_list[suggest]

            num = 0
            for field in FIELDS:
                sum = 0
                for token in FIX_TOKEN:
                    self.percentage_pies[suggest][field] = self.SECTORS[token][num] * self.FIX_TOKEN[token][suggest]
                    sum += self.percentage_pies[suggest][field]
                for crypto in FIX_CRYPTO:
                    self.percentage_pies[suggest][field] = self.SECTORS[crypto][num] * self.FIX_CRYPTO[crypto][suggest]
                    sum += self.percentage_pies[suggest][field]
                for esg in FIX_ESG:
                    self.percentage_pies[suggest][field] = self.SECTORS[esg][num] * self.FIX_ESG[esg][suggest]
                    sum += self.percentage_pies[suggest][field]
                self.percentage_pies[suggest][field] = sum
                num += 1

        for portfolio in self.portfolio_dict:
            num = (self.portfolio_dict[portfolio][len(self.portfolio_dict[portfolio])-1]-100)/100
            self.performance_of_each_portfolio.append(num)
