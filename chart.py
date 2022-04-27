import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
from yahoof import FinanceY


EXCEL_FILE = '/Users/dimitrisdiamantidis/Desktop/RoboAdvisor/Robo_Advisor.xlsx'

class Charts:

    def __init__(self):
        self.finance_data = FinanceY()
        self.selected_portfolio = []
        self.extras_chart = {}
        self.extras_name = []
        self.selected_portfolio = ""
        self.persentages = {}

    def create_percetages_dict(self):
        for token in self.finance_data.TOKEN:
            if self.finance_data.FIX_TOKEN[token][self.portfolio_name - 1] > 0:
                self.persentages[token] = self.finance_data.FIX_TOKEN[token][self.portfolio_name - 1]
        for crypto in self.finance_data.CRYPTOS:
            if self.finance_data.FIX_CRYPTO[crypto][self.portfolio_name - 1] > 0:
                self.persentages[crypto] = self.finance_data.FIX_CRYPTO[crypto][self.portfolio_name - 1]
        for esg in self.finance_data.ESG:
            if self.finance_data.FIX_ESG[esg][self.portfolio_name - 1] > 0:
                self.persentages[esg] = self.finance_data.FIX_ESG[esg][self.portfolio_name - 1]

    def portfolio_selection(self, risk_rate, extras):

        if risk_rate < 1.7:
            # Portfolio 1.
            self.selected_portfolio = self.finance_data.portfolio_dict[0]
            self.portfolio_name = 1
            self.portfolio_text = "Conservative"
            self.selected_esg = 6
            self.esg_text = "ESG Conservative"

        elif risk_rate <= 2.7:
            # Portfolio 2.
            self.selected_portfolio = self.finance_data.portfolio_dict[1]
            self.portfolio_name = 2
            self.portfolio_text = "Moderately Conservative"
            self.selected_esg = 7
            self.esg_text = "ESG Moderately Conservative"

        elif risk_rate <= 3.7:
            # Portfolio 3.
            self.selected_portfolio = self.finance_data.portfolio_dict[2]
            self.portfolio_name = 3
            self.portfolio_text = "Moderate"
            self.selected_esg = 8
            self.esg_text = "ESG Moderate"

        elif risk_rate <= 4.7:
            # Portfolio 4.
            self.selected_portfolio = self.finance_data.portfolio_dict[3]
            self.portfolio_name = 4
            self.portfolio_text = "Moderately Aggressive"
            self.selected_esg = 9
            self.esg_text = "ESG Moderately Aggressive"

        elif risk_rate <= 5:
            # Portfolio 5.
            self.selected_portfolio = self.finance_data.portfolio_dict[4]
            self.portfolio_name = 5
            self.portfolio_text = "Aggressive"
            self.selected_esg = 10
            self.esg_text = "ESG Aggressive"

        if extras == "Cryptos" or extras == "Cryptos- ESG":
            # Portfolios CRYPTO.
            if self.finance_data.exist_of_crypto == True:
                num_of_cryptos = 0
                for crypto in self.finance_data.CRYPTOS:
                    self.extras_chart[self.finance_data.number_of_suggestions_portfolios + num_of_cryptos] = self.finance_data.portfolio_dict[5]
                    self.extras_name.append(self.finance_data.number_of_suggestions_portfolios + num_of_cryptos)
                    self.selected_crypto = f"{self.finance_data.number_of_suggestions_portfolios + num_of_cryptos}"
                    num_of_cryptos += 1

        if extras == "ESG" or extras == "Cryptos- ESG":
            # Portfolios ESG.
            if self.finance_data.exist_of_esg == True:
                num_of_esg = len(self.finance_data.CRYPTOS)
                self.extras_chart[self.selected_esg] = self.finance_data.portfolio_dict[self.selected_esg]
                self.selected_esg_text = self.esg_text
        self.create_percetages_dict()

    def create_chart(self):
        # CREATE PLOT BASED ON CHART_LISTS.
        figure(figsize=(15, 20), dpi=100)  # Modify the large of chart.

        for j in self.extras_chart:  # EXTRA -----> CRYPTO AND ESG CHART <-----
            plt.plot(self.finance_data.recorded_days, self.extras_chart[j], label=j)

        plt.plot(self.finance_data.recorded_days, self.selected_portfolio, label=f"Portfolio {self.portfolio_name}", color="black")  # MY_PORTFOLIO PLOT

        plt.title("RoboAdvisor")
        plt.xlabel('DATE', fontsize=20)
        plt.ylabel('COST', fontsize=20)
        plt.show()

        # RING CHART.
        size_of_groups = [12, 11, 3, 30]

        # CREATE A PIE PLOT.
        plt.pie(size_of_groups)

        # ADD A CIRCLE AT THE CENTER TO TRANSFORM PIE PLOT TO A DONUT CHART.
        my_circle = plt.Circle((0, 0), 0.7, color='white')
        p = plt.gcf()
        p.gca().add_artist(my_circle)

        plt.show()
