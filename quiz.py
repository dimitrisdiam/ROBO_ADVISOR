from tkinter import *
import tkinter as tk
from chart import Charts
import numpy as np
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.patches import Circle
from tkinter import ttk
import tkinter.messagebox
from PIL import Image, ImageTk
import customtkinter
from matplotlib.gridspec import GridSpec







FONT_QUESTION = ('calibre', 28, 'bold')
FONT = ('calibre', 28)
FONT_SUB = ('calibre', 20)
answers = {
    1: ["Retirement",
        "General Investment",
        "A large purchase or expenditure (e.g. house, education, wedding, vacation)"],
    2: ["3",
        "3 to 5",
        "5 to 10",
        "more than 10 years from now"],
    3: ["I want to protect my account. I am willing to accept lower returns over the long-term to minimize the chance of loss at any given time.",
        "I want the best long-term performance. I would be willing to accept short-term losses in order to have higher returns in the long run."],
    4: ["age"],
    5: ["money"],
    6: ["money"],
    7: ["money"],
    8: ["money"],
    9: ["money"],
}

values = {
        1: [5, 3, 1],
        2: [1, 2, 3, 4],
        3: [1, 5],
        4: [5, 4, 3, 2, 1],
        5: [],
        6: [],
        7: [],
        8: [],
        9: [],
}

questions = [
    "What are you saving for?",
    "When do you want to achieve your goal?",
    "Investing is a trade-off between risk and reward.\nWhich statement do you most agree with:",
    "How old are you?",
    "How much is your net worth?\n(Your total savings, assets, etc)",
    "What is the initial amount that you want to invest?",
    "How much do you plan to save monthly towards retirement?",
    "Your annual total income:\n(An estimate of your gross annual income is required)",
    "Your annual total expenses:\n(An estimate of your gross annual income is required)",
]

crypto_question_text = "I agree most with the following statement: "

crypto_answers_text = [
    "I am well-informed about the risks and benefits of blockchain technology and cryptocurrencies in the financial world",
    "I am not well-informed about the risks and benefits of blockchain technology and cryptocurrencies in the financial world",
]

esg_question_text = "Which statement do you most agree with?"

esg_answers_text = [
    "I do believe that investments can contribute significantly to the formation of a more sustainable future",
    "I do not believe that investments can contribute significantly to the formation of a more sustainable future",
]

BACKGROUD_COLOR = f'#{146:02x}{186:02x}{146:02x}'
FRONTGROUND_COLOR = "white"


class Quiz:

    def __init__(self, window):

        self.root = window
        self.root.title("RoboAdvisor")
        self.root.geometry("1500x1000")
        self.root.configure(bg="white")

        self.q = tk.StringVar()
        self.crypto = IntVar()
        self.esg = IntVar()
        self.q.set("Retirement")
        self.total = 0
        self.question_num = 0
        self.net_worth = 0
        self.difference_money = 0
        self.risk_rate = 0
        self.entry_variable = IntVar()
        self.entry_variable_2 = IntVar()
        self.chart = Charts()
        self.extra_question = False
        self.command = ""

        self.finance = self.chart.finance_data
        self.first_canvas = Canvas(background=BACKGROUD_COLOR, width=1500, height=620, highlightthickness=0)

        self.first_step()

    def first_step(self):
        # -----PHOTO-----.
        image = Image.open("girl.jpeg")
        resize_image = image.resize((1500, 620))
        self.bg = ImageTk.PhotoImage(resize_image)
        self.label = Label(self.first_canvas, image=self.bg, bg=BACKGROUD_COLOR)
        self.label.place(x=-10, y=-10)


        self.first_canvas.pack()
        self.second_canvas = Canvas(width=500, height=300, background=BACKGROUD_COLOR, highlightthickness=0)   # rgb(211, 228, 205)
        self.first_label = Label(self.second_canvas, text="We help you invest in your future! - We help you to reach your financial goals", font=('calibre', 32, 'bold'), wraplength=500, background=BACKGROUD_COLOR, foreground=FRONTGROUND_COLOR)



        # -----BUTTON-----
        customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
        customtkinter.set_default_color_theme("green")  # Themes: blue (default), dark-blue, green


        self.button = customtkinter.CTkButton(master=self.second_canvas, text="Get Start", command=self.first_run, width=200, height=60, text_font=FONT)
        self.first_label.place(relx=0.5, rely=0.25, anchor=CENTER)
        self.button.place(relx=0.5, rely=0.75, anchor=tkinter.CENTER)
        self.second_canvas.place(x=30, y=400)

        # ----- SECOND IMAGE-----
        sec_image = Image.open("ROBO.png")
        self.sec_bg = ImageTk.PhotoImage(sec_image)

    def open_the_sub_btn(self):
        self.sub_btn.place_forget()
        if self.extra_question == False:
            self.sub_btn = customtkinter.CTkButton(master=self.root, text="Submit", command=self.submit, width=120, height=40, text_font=FONT_SUB)
        else:
            self.sub_btn = customtkinter.CTkButton(master=self.root, text="Submit", command=self.command, width=120, height=40, text_font=FONT_SUB)
        self.sub_btn.place(relx=0.5, rely=0.95, anchor=CENTER)

    def first_run(self):


        self.root.configure(background=BACKGROUD_COLOR)     #rgb(146, 186, 146)
        self.first_canvas.config(background=BACKGROUD_COLOR)
        self.second_canvas.place_forget()
        self.label.configure(image=self.sec_bg)
        self.label.place(relx=0.30, rely=0.05)
        self.first_label.place_forget()
        self.button.place_forget()
        self.second_canvas.place_forget()

        self.button.place_forget()
        self.q1 = tk.Label(self.root, font=FONT_QUESTION, text=questions[self.question_num], fg=FRONTGROUND_COLOR, bg=BACKGROUD_COLOR)
        self.q2 = tk.Label(self.root, font=FONT_QUESTION, text=questions[self.question_num], fg=FRONTGROUND_COLOR, bg=BACKGROUD_COLOR)

        self.entry = Entry(textvariable=self.entry_variable, highlightbackground=BACKGROUD_COLOR)
        self.q1_a1 = tk.Radiobutton(self.root, font=FONT, variable=self.q, text=answers[1][0], value=values[1][0], fg=FRONTGROUND_COLOR, bg=BACKGROUD_COLOR, command=self.open_the_sub_btn, wraplength=900)
        self.q1_a2 = tk.Radiobutton(self.root, font=FONT, variable=self.q, text=answers[1][1], value=values[1][1], fg=FRONTGROUND_COLOR, bg=BACKGROUD_COLOR, command=self.open_the_sub_btn, wraplength=900)
        self.q1_a3 = tk.Radiobutton(self.root, font=FONT, variable=self.q, text=answers[1][2], value=values[1][2], fg=FRONTGROUND_COLOR, bg=BACKGROUD_COLOR, command=self.open_the_sub_btn, wraplength=900)
        self.q1_a4 = tk.Radiobutton(self.root, font=FONT, variable=self.q, text="", value=4, fg=FRONTGROUND_COLOR, bg=BACKGROUD_COLOR, command=self.open_the_sub_btn, wraplength=900)

        self.q2_a1 = Entry(textvariable=self.entry_variable_2, highlightbackground=BACKGROUD_COLOR)


        # -----BUTTON-----
        customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
        customtkinter.set_default_color_theme("green")  # Themes: blue (default), dark-blue, green

        self.sub_btn = customtkinter.CTkButton(master=self.root, text="Submit", command=self.submit, width=120, height=40, text_font=FONT_SUB)

        self.entry.place_forget()
        self.q1.place(relx=0.5, rely=0.5, anchor=CENTER)
        self.q1_a1.place(relx=0.5, rely=0.57, anchor=CENTER)
        self.q1_a2.place(relx=0.5, rely=0.67, anchor=CENTER)
        self.q1_a3.place(relx=0.5, rely=0.77, anchor=CENTER)
        self.q1_a4.place_forget()

        #-----IF YOU NEED CHECKBOX UNCOMMENT THE ROWS BELOW-----
        # CHECKBOX ( OPTION )
        # self.crypto_box = Checkbutton(self.root, text="CRYPTO", variable=self.crypto, onvalue=1, offvalue=0, fg=FRONTGROUND_COLOR, bg=BACKGROUD_COLOR)
        # self.crypto_box.place(relx=0.45, rely=0.84, anchor=CENTER)
        # self.esg_box = Checkbutton(self.root, text="ESG", variable=self.esg, onvalue=1, offvalue=0, fg=FRONTGROUND_COLOR, bg=BACKGROUD_COLOR)
        # self.esg_box.place(relx=0.55, rely=0.84, anchor=CENTER)

    def clear(self):

        # ----- WINDOW CLEANING -----
        self.q1.place_forget()
        self.q1_a1.place_forget()
        self.q1_a2.place_forget()
        self.q1_a3.place_forget()
        self.q1_a4.place_forget()
        self.q2.place_forget()
        self.q2_a1.place_forget()
        self.entry.place_forget()
        self.sub_btn.place_forget()

        # ----- CALCULATE THE LAST VALUE -----
        if self.question_num == 8:
            difference_money = float((self.annual_income - self.amount_of_expenses - self.annual_savings)) / float(self.annual_income - self.amount_of_expenses)
            if difference_money <= 0.20:
                self.total += 1
            elif difference_money <= 0.40:
                self.total += 2
            elif difference_money <= 0.60:
                self.total += 3
            elif difference_money <= 0.80:
                self.total += 4
            elif difference_money <= 1.0:
                self.total += 5

        # ----- CALCULATE THE TOTAL RISK -----
        self.risk_rate = self.total/6

        # ----- PRESENT CRYPTO QUESTION WHEN RISK_RATE'S OVER 4.1 -----
        if self.risk_rate > 4.1:
            self.crypto_question()
        else:
            self.function = False
            self.crypto_answer = 0
            self.esg_question()

    def submit(self):
        again = False


        # ----- CHECK THE ANSWERS OF QUESTIONS & ADD THE APPROPRIATE VALUE TO TOTAL & VALUE CHECKING -----
        if self.question_num == 3:
            try:
                if int(self.entry.get()) == 0:
                    again = True
                    tkinter.messagebox.showinfo("Sorry..", "PLEASE, Give a Value.")
                elif int(self.entry.get()) <= 29:
                    self.total += 5
                elif int(self.entry.get()) < 35:
                    self.total += 4
                elif int(self.entry.get()) < 40:
                    self.total += 3
                elif int(self.entry.get()) < 55:
                    self.total += 2
                elif int(self.entry.get()) >= 55:
                    self.total += 1
            except ValueError:  # Check the entry text, in order to give us integer.
                again = True
                tkinter.messagebox.showinfo("Sorry..", "PLEASE, It has to be a number.")

        if self.question_num == 5:
            try:
                if float(self.entry.get()) > 0.0 and float(self.q2_a1.get()) > 0.0:   # Check the entry text, in order to give us value > 0.
                    self.net_worth = float(self.entry.get())
                    self.amount_for_invest = float(self.q2_a1.get())

                    if self.net_worth >= self.amount_for_invest:   # Check answer 5 > answer 6.
                        pass
                    else:
                        again = True
                        tkinter.messagebox.showinfo("Sorry..", "PLEASE, Your initial investment must be equal or less than your net worth")
                else:
                    again = True
                    tkinter.messagebox.showinfo("Sorry..", "PLEASE, Give a Value.")

            except ValueError:
                again = True
                tkinter.messagebox.showinfo("Sorry..", "PLEASE, It has to be a number.")

        if self.question_num == 5 and again == False:   # Check if everything is right to add the appropriate value to total.
            self.q2.place_forget()
            self.q2_a1.place_forget()
            difference_money = (self.net_worth - float(self.amount_for_invest)) / self.net_worth
            if difference_money <= 0.20:
                self.total += 1
            elif difference_money <= 0.40:
                self.total += 2
            elif difference_money <= 0.60:
                self.total += 3
            elif difference_money <= 0.80:
                self.total += 4
            elif difference_money <= 1.0:
                self.total += 5

        if self.question_num == 6:
            try:
                if float(self.entry.get()) > 0.0:
                    self.annual_savings = float(self.entry.get())/12   # Modify the value to monthly.
                else:
                    again = True
                    tkinter.messagebox.showinfo("Sorry..", "Please value has to be bigger than 0.")     # Check the entry text, in order to give us integer and not be 0.
            except ValueError:
                again = True
                tkinter.messagebox.showinfo("Sorry..", "Please value has to be Number.")  # Check the entry text, in order to give us integer and not be TEXT.

        if self.question_num == 8:
            try:
                if float(self.entry.get()) > 0.0 and float(self.q2_a1.get()) > 0.0:
                    self.annual_income = float(self.entry.get())/12
                    self.amount_of_expenses = float(self.q2_a1.get())/12
                    if self.annual_income > self.amount_of_expenses:     # Check answer 8 > answer 9.
                        pass
                    else:
                        again = True
                        tkinter.messagebox.showinfo("Sorry..", "PLEASE, Your annual expenses must be less than your annual income")
                else:
                    again = True
                    tkinter.messagebox.showinfo("Sorry..", "Give a Value")
            except ValueError:
                again = True
                tkinter.messagebox.showinfo("Sorry..", "PLEASE, It has to be a number.")    # Check the entry text, in order to give us integer and not be TEXT.

        if self.question_num == 8 and again == False:
            self.clear()

        # ----- PREPARATION FOR NEXT QUESTION -----
        if self.question_num <= 7 and again == False:   # Preparation until question 8.
            self.question_num += 1
            self.sub_btn.place_forget()

            # Auto-change the questions.
            self.q1.configure(text=questions[self.question_num])

            if len(answers[self.question_num+1]) == 1:  # Check every next question and prepare the number of answers.
                if len(answers[self.question_num]) > 1:
                    self.total += int(self.q.get())
                self.entry.place(relx=0.5, rely=0.57, anchor=CENTER)
                self.entry.delete(0, END)
                self.q1_a1.place_forget()    # Invisible answer.
                self.q1_a2.place_forget()
                self.q1_a3.place_forget()
                self.q1_a4.place_forget()
                self.sub_btn.place(relx=0.5, rely=0.86, anchor=CENTER)

                if self.question_num == 4:  # Special regulation for question 5.
                    self.question_num += 1
                    self.q2.configure(text=questions[self.question_num])
                    self.q2.place(relx=0.5, rely=0.7, anchor=CENTER)
                    self.q2_a1.place(relx=0.5, rely=0.75, anchor=CENTER)
                    self.q2_a1.delete(0, END)

                if self.question_num == 7:  # Special regulation for question 8.
                    self.question_num += 1
                    self.q2.configure(text=questions[self.question_num])
                    self.q2.place(relx=0.5, rely=0.7, anchor=CENTER)
                    self.q2_a1.place(relx=0.5, rely=0.79, anchor=CENTER)
                    self.q2_a1.delete(0, END)


            elif len(answers[self.question_num+1]) == 2:
                self.total += int(self.q.get())
                self.q1_a1.configure(text=answers[self.question_num+1][0], value=values[self.question_num+1][0])
                self.q1_a2.configure(text=answers[self.question_num+1][1], value=values[self.question_num+1][1])
                self.q1_a1.place(relx=0.5, rely=0.63, anchor=CENTER)
                self.q1_a2.place(relx=0.5, rely=0.78, anchor=CENTER)
                self.q1_a3.place_forget()
                self.q1_a4.place_forget()

            elif len(answers[self.question_num+1]) == 3:
                self.total += int(self.q.get())
                self.q1_a1.configure(text=answers[self.question_num + 1][0], value=values[self.question_num+1][0])
                self.q1_a2.configure(text=answers[self.question_num + 1][1], value=values[self.question_num+1][1])
                self.q1_a3.configure(text=answers[self.question_num+1][2], value=values[self.question_num+1][2])
                self.q1_a3.place(relx=0.5, rely=0.77, anchor=CENTER)
                self.q1_a4.place_forget()

            elif len(answers[self.question_num+1]) == 4:
                self.total += int(self.q.get())
                self.q1_a1.configure(text=answers[self.question_num + 1][0], value=values[self.question_num+1][0])
                self.q1_a2.configure(text=answers[self.question_num + 1][1], value=values[self.question_num+1][1])

                self.q1_a3.configure(text=answers[self.question_num + 1][2], value=values[self.question_num+1][2])
                self.q1_a3.place(relx=0.5, rely=0.77, anchor=CENTER)
                self.q1_a4.configure(text=answers[self.question_num + 1][3], value=values[self.question_num+1][3])
                self.q1_a4.place(relx=0.5, rely=0.87, anchor=CENTER)


    def final_letter(self):


        self.graphs()

        self.final_portfolio_letter = [f"""Your risk profile, which was determined according to your answers, is conservative and we suggest you a portfolio consisting of ETFs that follow stocks in the following industries:\n\n‣  Technology ({float("{0:.2f}".format((self.appropriate_portfolios[f"PORTFOLIO: {self.chart.portfolio_name}"]["Technology"]*100)))}% of the portfolio)\n‣  Healthcare ({float("{0:.2f}".format((self.appropriate_portfolios[f"PORTFOLIO: {self.chart.portfolio_name}"]["Healthcare"]*100)))}% of the portfolio)\n‣  Industrials ({float("{0:.2f}".format((self.appropriate_portfolios[f"PORTFOLIO: {self.chart.portfolio_name}"]["Industrials"]*100)))}% of the portfolio)\n‣  Financial Services ({float("{0:.2f}".format((self.appropriate_portfolios[f"PORTFOLIO: {self.chart.portfolio_name}"]["Financial Services"]*100)))}% of the portfolio)\n‣  Consumer Cyclical ({float("{0:.2f}".format((self.appropriate_portfolios[f"PORTFOLIO: {self.chart.portfolio_name}"]["Consumer Cyclical"]*100)))}% of the portfolio)\n\nThe distribution of ETFs in the suggested portfolio may be seen in the pie chart. \n\n‣  50% of the portfolio is distributed to ETFs following stocks\n‣  50% of the portfolio is distributed to ETFs following bonds\n\nThe dynamics of the suggested portfolio over the past 3 years are presented on the line graph. We suggest this portfolio matches your expectations, offering the highest return considering the level of risk you are ready to bear.\nThe performance of the suggested portfolio the last 3 years is {float("{0:.2f}".format((self.finance.performance_of_each_portfolio[self.chart.portfolio_name-1]*100)))}%.""",
                                       f"""Your risk profile, which was determined according to your answers, is moderately conservative and we suggest you a portfolio consisting of ETFs that follow stocks in the following industries:\n\n‣  Technology ({float("{0:.2f}".format((self.appropriate_portfolios[f"PORTFOLIO: {self.chart.portfolio_name}"]["Technology"]*100)))}% of the portfolio)\n‣  Healthcare ({float("{0:.2f}".format((self.appropriate_portfolios[f"PORTFOLIO: {self.chart.portfolio_name}"]["Healthcare"]*100)))}% of the portfolio)\n‣  Industrials ({float("{0:.2f}".format((self.appropriate_portfolios[f"PORTFOLIO: {self.chart.portfolio_name}"]["Industrials"]*100)))}% of the portfolio)\n‣  Financial Services ({float("{0:.2f}".format((self.appropriate_portfolios[f"PORTFOLIO: {self.chart.portfolio_name}"]["Financial Services"]*100)))}% of the portfolio)\n‣  Consumer Cyclical ({float("{0:.2f}".format((self.appropriate_portfolios[f"PORTFOLIO: {self.chart.portfolio_name}"]["Consumer Cyclical"]*100)))}% of the portfolio)\n\nThe distribution of ETFs in the suggested portfolio may be seen in the pie chart. \n\n‣  60% of the portfolio is distributed to ETFs following stocks\n‣  40% of the portfolio is distributed to ETFs following bonds\n\nThe dynamics of the suggested portfolio over the past 3 years are presented on the line graph. We suggest this portfolio matches your expectations, offering the highest return considering the level of risk you are ready to bear.\nThe performance of the suggested portfolio the last 3 years is {float("{0:.2f}".format((self.finance.performance_of_each_portfolio[self.chart.portfolio_name-1]*100)))}%.""",
                                       f"""Your risk profile, which was determined according to your answers, is moderate and we suggest you a portfolio consisting of ETFs that follow stocks in the following industries:\n\n‣  Technology ({float("{0:.2f}".format((self.appropriate_portfolios[f"PORTFOLIO: {self.chart.portfolio_name}"]["Technology"]*100)))}% of the portfolio)\n‣  Healthcare ({float("{0:.2f}".format((self.appropriate_portfolios[f"PORTFOLIO: {self.chart.portfolio_name}"]["Healthcare"]*100)))}% of the portfolio)\n‣  Industrials ({float("{0:.2f}".format((self.appropriate_portfolios[f"PORTFOLIO: {self.chart.portfolio_name}"]["Industrials"]*100)))}% of the portfolio)\n‣  Financial Services ({float("{0:.2f}".format((self.appropriate_portfolios[f"PORTFOLIO: {self.chart.portfolio_name}"]["Financial Services"]*100)))}% of the portfolio)\n‣  Consumer Cyclical ({float("{0:.2f}".format((self.appropriate_portfolios[f"PORTFOLIO: {self.chart.portfolio_name}"]["Consumer Cyclical"]*100)))}% of the portfolio)\n\nThe distribution of ETFs in the suggested portfolio may be seen in the pie chart. \n\n‣  75% of the portfolio is distributed to ETFs following stocks\n‣  25% of the portfolio is distributed to ETFs following bonds\n\nThe dynamics of the suggested portfolio over the past 3 years are presented on the line graph. We suggest this portfolio matches your expectations, offering the highest return considering the level of risk you are ready to bear.\nThe performance of the suggested portfolio the last 3 years is {float("{0:.2f}".format((self.finance.performance_of_each_portfolio[self.chart.portfolio_name-1]*100)))}%.""",
                                       f"""Your risk profile, which was determined according to your answers, is moderately aggressive and we suggest you a portfolio consisting of ETFs that follow stocks in the following industries:\n\n‣  Technology ({float("{0:.2f}".format((self.appropriate_portfolios[f"PORTFOLIO: {self.chart.portfolio_name}"]["Technology"]*100)))}% of the portfolio)\n‣  Healthcare ({float("{0:.2f}".format((self.appropriate_portfolios[f"PORTFOLIO: {self.chart.portfolio_name}"]["Healthcare"]*100)))}% of the portfolio)\n‣  Industrials ({float("{0:.2f}".format((self.appropriate_portfolios[f"PORTFOLIO: {self.chart.portfolio_name}"]["Industrials"]*100)))}% of the portfolio)\n‣  Financial Services ({float("{0:.2f}".format((self.appropriate_portfolios[f"PORTFOLIO: {self.chart.portfolio_name}"]["Financial Services"]*100)))}% of the portfolio)\n‣  Consumer Cyclical ({float("{0:.2f}".format((self.appropriate_portfolios[f"PORTFOLIO: {self.chart.portfolio_name}"]["Consumer Cyclical"]*100)))}% of the portfolio)\n\nThe distribution of ETFs in the suggested portfolio may be seen in the pie chart. \n\n‣  85% of the portfolio is distributed to ETFs following stocks\n‣  15% of the portfolio is distributed to ETFs following bonds\n\nThe dynamics of the suggested portfolio over the past 3 years are presented on the line graph. We suggest this portfolio matches your expectations, offering the highest return considering the level of risk you are ready to bear.\nThe performance of the suggested portfolio the last 3 years is {float("{0:.2f}".format((self.finance.performance_of_each_portfolio[self.chart.portfolio_name-1]*100)))}%.""",
                                       f"""Your risk profile, which was determined according to your answers, is aggressive and we suggest you a portfolio consisting of ETFs that follow stocks in the following industries:\n\n‣  Technology ({float("{0:.2f}".format((self.appropriate_portfolios[f"PORTFOLIO: {self.chart.portfolio_name}"]["Technology"]*100)))}% of the portfolio)\n‣  Healthcare ({float("{0:.2f}".format((self.appropriate_portfolios[f"PORTFOLIO: {self.chart.portfolio_name}"]["Healthcare"]*100)))}% of the portfolio)\n‣  Industrials ({float("{0:.2f}".format((self.appropriate_portfolios[f"PORTFOLIO: {self.chart.portfolio_name}"]["Industrials"]*100)))}% of the portfolio)\n‣  Financial Services ({float("{0:.2f}".format((self.appropriate_portfolios[f"PORTFOLIO: {self.chart.portfolio_name}"]["Financial Services"]*100)))}% of the portfolio)\n‣  Consumer Cyclical ({float("{0:.2f}".format((self.appropriate_portfolios[f"PORTFOLIO: {self.chart.portfolio_name}"]["Consumer Cyclical"]*100)))}% of the portfolio)\n\nThe distribution of ETFs in the suggested portfolio may be seen in the pie chart. \n\n‣  100% of the portfolio is distributed to ETFs following stocks\n\nThe dynamics of the suggested portfolio over the past 3 years are presented on the line graph. We suggest this portfolio matches your expectations, offering the highest return considering the level of risk you are ready to bear.\nThe performance of the suggested portfolio the last 3 years is {float("{0:.2f}".format((self.finance.performance_of_each_portfolio[self.chart.portfolio_name-1]*100)))}%.""", ]
        self.final_ESG_letter = [
            f"""Your risk profile, which was determined according to your answers, is conservative and we suggest you a portfolio consisting of basic ETFs that follow stocks in the following industries:\n\n‣  Technology ({float("{0:.2f}".format((self.appropriate_portfolios[f"PORTFOLIO: {self.chart.portfolio_name}"]["Technology"]*100)))}% of the portfolio)\n‣  Healthcare ({float("{0:.2f}".format((self.appropriate_portfolios[f"PORTFOLIO: {self.chart.portfolio_name}"]["Healthcare"]*100)))}% of the portfolio)\n‣  Industrials ({float("{0:.2f}".format((self.appropriate_portfolios[f"PORTFOLIO: {self.chart.portfolio_name}"]["Industrials"]*100)))}% of the portfolio)\n‣  Financial Services ({float("{0:.2f}".format((self.appropriate_portfolios[f"PORTFOLIO: {self.chart.portfolio_name}"]["Financial Services"]*100)))}% of the portfolio)\n‣  Consumer Cyclical ({float("{0:.2f}".format((self.appropriate_portfolios[f"PORTFOLIO: {self.chart.portfolio_name}"]["Consumer Cyclical"]*100)))}% of the portfolio)\n\nThe distribution of ETFs in the basic suggested portfolio consists of: \n\n‣  50% of the portfolio is distributed to ETFs following stocks\n‣  50% of the portfolio is distributed to ETFs following bonds\n\nAs far as you are also interested in ESG, we also offer you the second portfolio, which consists of:\n\n‣  40% of the basic portfolio\n‣  60% of ESG ETFs\n\nThe dynamics over the past 3 years and the distribution of the two suggested portfolios may also be seen on the line graph and in the pie chart respectively.The distribution of the basic portfolio may be seen in the left pie chart and the second portfolio in the right pie chart.We suggest these portfolios match your expectations, offering the highest return considering the level of risk you are ready to bear.\nThe performance of the suggested portfolios the last 3 years is {float("{0:.2f}".format((self.finance.performance_of_each_portfolio[self.chart.portfolio_name-1]*100)))}% and {float("{0:.2f}".format((self.finance.performance_of_each_portfolio[self.chart.portfolio_name+5]*100)))}% respectively.""",
            f"""Your risk profile, which was determined according to your answers, is moderately conservative and we suggest you a portfolio consisting of basic ETFs that follow stocks in the following industries:\n\n‣  Technology ({float("{0:.2f}".format((self.appropriate_portfolios[f"PORTFOLIO: {self.chart.portfolio_name}"]["Technology"]*100)))}% of the portfolio)\n‣  Healthcare ({float("{0:.2f}".format((self.appropriate_portfolios[f"PORTFOLIO: {self.chart.portfolio_name}"]["Healthcare"]*100)))}% of the portfolio)\n‣  Industrials ({float("{0:.2f}".format((self.appropriate_portfolios[f"PORTFOLIO: {self.chart.portfolio_name}"]["Industrials"]*100)))}% of the portfolio)\n‣  Financial Services ({float("{0:.2f}".format((self.appropriate_portfolios[f"PORTFOLIO: {self.chart.portfolio_name}"]["Financial Services"]*100)))}% of the portfolio)\n‣  Consumer Cyclical ({float("{0:.2f}".format((self.appropriate_portfolios[f"PORTFOLIO: {self.chart.portfolio_name}"]["Consumer Cyclical"]*100)))}% of the portfolio)\n\nThe distribution of ETFs in the basic suggested portfolio consists of:\n\n‣  60% of the portfolio is distributed to ETFs following stocks\n‣  40% of the portfolio is distributed to ETFs following bonds\n\nAs far as you are also interested in ESG, we also offer you the second portfolio, which consists of:\n\n‣  40% of the basic portfolio\n‣  60% of ESG ETFs\n\nThe dynamics over the past 3 years and the distribution of the two suggested portfolios may also be seen on the line graph and in the pie chart respectively.The distribution of the basic portfolio may be seen in the left pie chart and the second portfolio in the right pie chart.We suggest these portfolios match your expectations, offering the highest return considering the level of risk you are ready to bear.\nThe performance of the suggested portfolios the last 3 years is {float("{0:.2f}".format((self.finance.performance_of_each_portfolio[self.chart.portfolio_name-1]*100)))}% and {float("{0:.2f}".format((self.finance.performance_of_each_portfolio[self.chart.portfolio_name+5]*100)))}% respectively.""",
            f"""Your risk profile, which was determined according to your answers, is moderate and we suggest you a portfolio consisting of basic ETFs that follow stocks in the following industries:\n\n‣  Technology ({float("{0:.2f}".format((self.appropriate_portfolios[f"PORTFOLIO: {self.chart.portfolio_name}"]["Technology"]*100)))}% of the portfolio)\n‣  Healthcare ({float("{0:.2f}".format((self.appropriate_portfolios[f"PORTFOLIO: {self.chart.portfolio_name}"]["Healthcare"]*100)))}% of the portfolio)\n‣  Industrials ({float("{0:.2f}".format((self.appropriate_portfolios[f"PORTFOLIO: {self.chart.portfolio_name}"]["Industrials"]*100)))}% of the portfolio)\n‣  Financial Services ({float("{0:.2f}".format((self.appropriate_portfolios[f"PORTFOLIO: {self.chart.portfolio_name}"]["Financial Services"]*100)))}% of the portfolio)\n‣  Consumer Cyclical ({float("{0:.2f}".format((self.appropriate_portfolios[f"PORTFOLIO: {self.chart.portfolio_name}"]["Consumer Cyclical"]*100)))}% of the portfolio)\n\nThe distribution of ETFs in the basic suggested portfolio consists of:\n\n‣  75% of the portfolio is distributed to ETFs following stocks\n‣  25% of the portfolio is distributed to ETFs following bonds\n\nAs far as you are also interested in ESG, we also offer you the second portfolio, which consists of:\n\n‣  40% of the basic portfolio\n‣  60% of ESG ETFs\n\nThe dynamics over the past 3 years and the distribution of the two suggested portfolios may also be seen on the line graph and in the pie chart respectively.The distribution of the basic portfolio may be seen in the left pie chart and the second portfolio in the right pie chart.We suggest these portfolios match your expectations, offering the highest return considering the level of risk you are ready to bear.\nThe performance of the suggested portfolios the last 3 years is {float("{0:.2f}".format((self.finance.performance_of_each_portfolio[self.chart.portfolio_name-1]*100)))}% and {float("{0:.2f}".format((self.finance.performance_of_each_portfolio[self.chart.portfolio_name+5]*100)))}% respectively.""",
            f"""Your risk profile, which was determined according to your answers, is moderately aggressive and we suggest you a portfolio consisting of basic ETFs that follow stocks in the following industries:\n\n‣  Technology ({float("{0:.2f}".format((self.appropriate_portfolios[f"PORTFOLIO: {self.chart.portfolio_name}"]["Technology"]*100)))}% of the portfolio)\n‣  Healthcare ({float("{0:.2f}".format((self.appropriate_portfolios[f"PORTFOLIO: {self.chart.portfolio_name}"]["Healthcare"]*100)))}% of the portfolio)\n‣  Industrials ({float("{0:.2f}".format((self.appropriate_portfolios[f"PORTFOLIO: {self.chart.portfolio_name}"]["Industrials"]*100)))}% of the portfolio)\n‣  Financial Services ({float("{0:.2f}".format((self.appropriate_portfolios[f"PORTFOLIO: {self.chart.portfolio_name}"]["Financial Services"]*100)))}% of the portfolio)\n‣  Consumer Cyclical ({float("{0:.2f}".format((self.appropriate_portfolios[f"PORTFOLIO: {self.chart.portfolio_name}"]["Consumer Cyclical"]*100)))}% of the portfolio)\n\nThe distribution of ETFs in the basic suggested portfolio consists of: \n\n‣  85% of the portfolio is distributed to ETFs following stocks\n‣  15% of the portfolio is distributed to ETFs following bonds\n\nAs far as you are also interested in ESG, we also offer you the second portfolio, which consists of:\n\n‣  40% of the basic portfolio\n‣  60% of ESG ETFs\n\nThe dynamics over the past 3 years and the distribution of the two suggested portfolios may also be seen on the line graph and in the pie chart respectively.The distribution of the basic portfolio may be seen in the left pie chart and the second portfolio in the right pie chart.We suggest these portfolios match your expectations, offering the highest return considering the level of risk you are ready to bear.\nThe performance of the suggested portfolios the last 3 years is {float("{0:.2f}".format((self.finance.performance_of_each_portfolio[self.chart.portfolio_name-1]*100)))}% and {float("{0:.2f}".format((self.finance.performance_of_each_portfolio[self.chart.portfolio_name+5]*100)))}% respectively.""",
            f"""Your risk profile, which was determined according to your answers, is aggressive and we suggest you a portfolio consisting of basic ETFs that follow stocks in the following industries:\n\n‣  Technology ({float("{0:.2f}".format((self.appropriate_portfolios[f"PORTFOLIO: {self.chart.portfolio_name}"]["Technology"]*100)))}% of the portfolio)\n‣  Healthcare ({float("{0:.2f}".format((self.appropriate_portfolios[f"PORTFOLIO: {self.chart.portfolio_name}"]["Healthcare"]*100)))}% of the portfolio)\n‣  Industrials ({float("{0:.2f}".format((self.appropriate_portfolios[f"PORTFOLIO: {self.chart.portfolio_name}"]["Industrials"]*100)))}% of the portfolio)\n‣  Financial Services ({float("{0:.2f}".format((self.appropriate_portfolios[f"PORTFOLIO: {self.chart.portfolio_name}"]["Financial Services"]*100)))}% of the portfolio)\n‣  Consumer Cyclical ({float("{0:.2f}".format((self.appropriate_portfolios[f"PORTFOLIO: {self.chart.portfolio_name}"]["Consumer Cyclical"]*100)))}% of the portfolio)\n\nThe distribution of ETFs in the basic suggested portfolio consists of: \n\n‣  100% of the portfolio is distributed to ETFs following stocks\n\nAs far as you are also interested in ESG, we also offer you the second portfolio, which consists of:\n\n‣  40% of the basic portfolio\n‣  60% of ESG ETFs\n\nThe dynamics over the past 3 years and the distribution of the two suggested portfolios may also be seen on the line graph and in the pie chart respectively.The distribution of the basic portfolio may be seen in the left pie chart and the second portfolio in the right pie chart.We suggest these portfolios match your expectations, offering the highest return considering the level of risk you are ready to bear.\nThe performance of the suggested portfolios the last 3 years is {float("{0:.2f}".format((self.finance.performance_of_each_portfolio[self.chart.portfolio_name-1]*100)))}% and {float("{0:.2f}".format((self.finance.performance_of_each_portfolio[self.chart.portfolio_name+5]*100)))}% respectively.""",
        ]
        self.final_MIX_letter = [
            f"""Your risk profile, which was determined according to your answers, is moderately aggressive and we suggest you a portfolio consisting of basic ETFs that follow stocks in the following industries:\n\n‣  Technology ({float("{0:.2f}".format((self.appropriate_portfolios[f"PORTFOLIO: {self.chart.portfolio_name}"]["Technology"]*100)))}% of the portfolio)\n‣  Healthcare ({float("{0:.2f}".format((self.appropriate_portfolios[f"PORTFOLIO: {self.chart.portfolio_name}"]["Healthcare"]*100)))}% of the portfolio)\n‣  Industrials ({float("{0:.2f}".format((self.appropriate_portfolios[f"PORTFOLIO: {self.chart.portfolio_name}"]["Industrials"]*100)))}% of the portfolio)\n‣  Financial Services ({float("{0:.2f}".format((self.appropriate_portfolios[f"PORTFOLIO: {self.chart.portfolio_name}"]["Financial Services"]*100)))}% of the portfolio)\n‣  Consumer Cyclical ({float("{0:.2f}".format((self.appropriate_portfolios[f"PORTFOLIO: {self.chart.portfolio_name}"]["Consumer Cyclical"]*100)))}% of the portfolio)\n\nThe distribution of ETFs in the basic suggested portfolio consists of: \n\n‣  85% of the portfolio is distributed to ETFs following stocks\n‣  15% of the portfolio is distributed to ETFs following bonds\n\nAs far as you are also interested in ESG and cryptofinance, we also offer you additional portfolios, which consist of:\n\n‣  90% of the basic portfolio\n‣  10% of cryptofinance ETFs\n\nAnd of:\n\n‣  40% of the basic portfolio\n‣  60% of ESG ETFs\n\nThe dynamics over the past 3 years and the distribution of the three suggested portfolios may also be seen on the line graph and in the pie chart respectively.The distribution of the basic portfolio may be seen in the left pie chart, the Crypto portfolio in the middle pie chart and the ESG portfolio in the right pie chart.We suggest these portfolios match your expectations, offering the highest return considering the level of risk you are ready to bear.\nThe performance of the suggested portfolios the last 3 years is {float("{0:.2f}".format((self.finance.performance_of_each_portfolio[self.chart.portfolio_name-1]*100)))}%, {float("{0:.2f}".format((self.finance.performance_of_each_portfolio[5]*100)))}% and {float("{0:.2f}".format((self.finance.performance_of_each_portfolio[self.chart.portfolio_name+5]*100)))}% respectively.""",
            f"""Your risk profile, which was determined according to your answers, is aggressive and we suggest you a portfolio consisting of basic ETFs that follow stocks in the following industries:\n\n‣  Technology ({float("{0:.2f}".format((self.appropriate_portfolios[f"PORTFOLIO: {self.chart.portfolio_name}"]["Technology"]*100)))}% of the portfolio)\n‣  Healthcare ({float("{0:.2f}".format((self.appropriate_portfolios[f"PORTFOLIO: {self.chart.portfolio_name}"]["Healthcare"]*100)))}% of the portfolio)\n‣  Industrials ({float("{0:.2f}".format((self.appropriate_portfolios[f"PORTFOLIO: {self.chart.portfolio_name}"]["Industrials"]*100)))}% of the portfolio)\n‣  Financial Services ({float("{0:.2f}".format((self.appropriate_portfolios[f"PORTFOLIO: {self.chart.portfolio_name}"]["Financial Services"]*100)))}% of the portfolio)\n‣  Consumer Cyclical ({float("{0:.2f}".format((self.appropriate_portfolios[f"PORTFOLIO: {self.chart.portfolio_name}"]["Consumer Cyclical"]*100)))}% of the portfolio)\n\nThe distribution of ETFs in the basic suggested portfolio consists of: \n\n‣  100% of the portfolio is distributed to ETFs following stocks\n\nAs far as you are also interested in ESG and cryptofinance, we also offer you additional portfolios, which consist of:\n\n‣  90% of the basic portfolio\n‣  10% of cryptofinance ETFs\n\nAnd of:\n\n‣  40% of the basic portfolio\n‣  60% of ESG ETFs\n\nThe dynamics over the past 3 years and the distribution of the three suggested portfolios may also be seen on the line graph and in the pie chart respectively.The distribution of the basic portfolio may be seen in the left pie chart, the Crypto portfolio in the middle pie chart and the ESG portfolio in the right pie chart.We suggest these portfolios match your expectations, offering the highest return considering the level of risk you are ready to bear.\nThe performance of the suggested portfolios the last 3 years is {float("{0:.2f}".format((self.finance.performance_of_each_portfolio[self.chart.portfolio_name-1]*100)))}%, {float("{0:.2f}".format((self.finance.performance_of_each_portfolio[5]*100)))}% and {float("{0:.2f}".format((self.finance.performance_of_each_portfolio[self.chart.portfolio_name+5]*100)))}% respectively.""",
                ]
        self.final_CRYPTO_letter = [
            f"""Your risk profile, which was determined according to your answers, is aggressive and we suggest you a portfolio consisting of basic ETFs that follow stocks in the following industries:\n\n‣  Technology ({float("{0:.2f}".format((self.appropriate_portfolios[f"PORTFOLIO: {self.chart.portfolio_name}"]["Technology"]*100)))}% of the portfolio)\n‣  Healthcare ({float("{0:.2f}".format((self.appropriate_portfolios[f"PORTFOLIO: {self.chart.portfolio_name}"]["Healthcare"]*100)))}% of the portfolio)\n‣  Industrials ({float("{0:.2f}".format((self.appropriate_portfolios[f"PORTFOLIO: {self.chart.portfolio_name}"]["Industrials"]*100)))}% of the portfolio)\n‣  Financial Services ({float("{0:.2f}".format((self.appropriate_portfolios[f"PORTFOLIO: {self.chart.portfolio_name}"]["Financial Services"]*100)))}% of the portfolio)\n‣  Consumer Cyclical ({float("{0:.2f}".format((self.appropriate_portfolios[f"PORTFOLIO: {self.chart.portfolio_name}"]["Consumer Cyclical"]*100)))}% of the portfolio)\n\nThe distribution of ETFs in the basic suggested portfolio consists of: \n\n‣  100% of the portfolio is distributed to ETFs following stocks\n\nAs far as you are also interested in cryptofinance, we also offer you the second portfolio, which consists of:\n\n‣  90% of the basic portfolio\n‣  10% of Bitcoin-linked ETF\n\nThe dynamics over the past 3 years and the distribution of the two suggested portfolios may also be seen on the line graph and in the pie chart respectively.The distribution of the basic portfolio may be seen in the left pie chart and the second portfolio in the right pie chart.We suggest these portfolios match your expectations, offering the highest return considering the level of risk you are ready to bear.\nThe performance of the suggested portfolios the last 3 years is {float("{0:.2f}".format((self.finance.performance_of_each_portfolio[self.chart.portfolio_name-1]*100)))}% and {float("{0:.2f}".format((self.finance.performance_of_each_portfolio[5]*100)))}% respectively.""",
        ]

        # ----- PORTFOLIO TEXT -----
        portfolio_text = self.final_portfolio_letter[self.chart.portfolio_name - 1]
        esg_text = self.final_ESG_letter[self.chart.portfolio_name - 1]
        crypto_text = self.final_CRYPTO_letter[0]

        self.container = ttk.Frame(self.root)
        self.text_canvas = Canvas(self.container, width=928, height=300, background="white", highlightthickness=0)
        scroll = ttk.Scrollbar(self.container, orient="vertical", command=self.text_canvas.yview)
        scrollable_frame = ttk.Frame(self.container)

        scrollable_frame.bind(
            "<Configure>",
            lambda e: self.text_canvas.configure(
                scrollregion=self.text_canvas.bbox("all")
            )
        )

        self.text_canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

        self.text_canvas.configure(yscrollcommand=scroll.set)

        self.text_canvas.configure(yscrollcommand=scroll.set, highlightthickness=0)

        self.container.place(x=250, y=490)
        self.text_canvas.pack(side="left", fill="both", expand=True)
        scroll.pack(side="right", fill="y")

        final = Label(scrollable_frame, text=f"", wraplength=925, bg="white", fg="black", font=('calibre', 20), justify=LEFT)

        if self.extras == "Cryptos- ESG":
            if self.risk_rate <=4.7:
                final.configure(text=f"{self.final_MIX_letter[0]}")
            else:
                final.configure(text=f"{self.final_MIX_letter[1]}")
        elif self.extras == "Cryptos":
            final.configure(text=f"{crypto_text}")
        elif self.extras == "ESG":
            final.configure(text=f"{esg_text}")
        else:
            final.configure(text=f"{portfolio_text}")

        final.pack()

    def crypto_question(self):
        self.extra_question = True
        self.command = self.esg_question

        self.q1.configure(text=crypto_question_text)
        self.q1_a1.configure(text=crypto_answers_text[0], value=1, command=self.open_the_sub_btn, wraplength=900)
        self.q1_a2.configure(text=crypto_answers_text[1], value=0, command=self.open_the_sub_btn, wraplength=900)

        self.q1.place(relx=0.5, rely=0.5, anchor=CENTER)
        self.q1_a1.place(relx=0.5, rely=0.63, anchor=CENTER)
        self.q1_a2.place(relx=0.5, rely=0.78, anchor=CENTER)

        self.sub_btn.configure(command=self.esg_question)
        self.function = True

    def esg_question(self):
        self.extra_question = True

        self.command = self.cryptos_and_esg
        self.sub_btn.place_forget()

        if self.function:   # Check if user decided to invest on cryptos.
            self.crypto_answer = int(self.q.get())

        self.q1.configure(text=esg_question_text)
        self.q1_a1.configure(text=esg_answers_text[0], value=1, command=self.open_the_sub_btn)
        self.q1_a2.configure(text=esg_answers_text[1], value=0, command=self.open_the_sub_btn)

        self.q1.place(relx=0.5, rely=0.5, anchor=CENTER)
        self.q1_a1.place(relx=0.5, rely=0.63, anchor=CENTER)
        self.q1_a2.place(relx=0.5, rely=0.78, anchor=CENTER)

        self.sub_btn.configure(command=self.cryptos_and_esg)

    def cryptos_and_esg(self):

        self.q1.place_forget()
        self.q1_a1.place_forget()
        self.q1_a2.place_forget()
        self.sub_btn.place_forget()

        customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
        customtkinter.set_default_color_theme("green")  # Themes: blue (default), dark-blue, green

        self.sub_btn = customtkinter.CTkButton(master=self.root, text="Restart", command=self.restart, width=120,
                                               height=40, text_font=FONT_SUB)
        self.sub_btn.place(x=675, y=820)
        self.esg_answer = int(self.q.get())

        # ----- CHECK THE ANSWERS ABOUT CRYPTOS AND ESG -----
        if self.crypto_answer == 1 and self.esg_answer == 1:
            self.extras = "Cryptos- ESG"
        elif self.crypto_answer == 1:
            self.extras = "Cryptos"
        elif self.esg_answer == 1:
            self.extras = "ESG"
        else:
            self.extras = ""

        self.chart.portfolio_selection(self.risk_rate, self.extras)
        self.final_letter()
        return self.risk_rate

    def graphs(self):

        # ----- CHARTS & LETTER -----
        # ----- CREATE PLOT BASED ON CHART_LISTS -----
        v = np.array(self.chart.selected_portfolio)
        dates = self.finance.recorded_days
        self.fig = Figure((29, 13), dpi=55)
        self.fig.patch.set_facecolor('#92BA92')

        if self.extras == "Cryptos- ESG":
            self.row = 2
            self.column = 3
            self.num_of_pies = 3
            self.pies_row = [-1, -1, 1]
            self.pies_column = [0, -2, -1]

        elif self.extras == "Cryptos":
            self.row = 2
            self.column = 2
            self.num_of_pies = 2
            self.pies_row = [-1, -1]
            self.pies_column = [0, -1]

        elif self.extras == "ESG":
            self.row = 2
            self.column = 2
            self.num_of_pies = 2
            self.pies_row = [-1, -1]
            self.pies_column = [0, -1]

        else:
            self.row = 2
            self.column = 1
            self.num_of_pies = 1
            self.pies_row = [-1]
            self.pies_column = [0]

        self.gs = GridSpec(self.row, self.column, figure=self.fig)
        self.gs.update(wspace=0.4, hspace=0.4)

        self.a = self.fig.add_subplot(self.gs[0, :])

        for j in self.chart.extras_chart:
            k = np.array(self.chart.extras_chart[j])
            self.a.plot(dates, k)  # Blue plot.

        self.a.plot(dates, v, 'black')  # Blue plot.
        self.a.tick_params(axis='x', labelsize=15, rotation=20)
        self.a.tick_params(axis='y', labelsize=15)
        self.a.set_title("Suggested Portfolios", fontsize=20)
        self.a.set_ylabel("Price", fontsize=20)
        self.a.set_xlabel("Date", fontsize=20)

        # DICTIONARY ABOUT PIES.
        self.title_of_pie = []
        self.appropriate_portfolios = {}
        self.appropriate_portfolios[f"PORTFOLIO: {self.chart.portfolio_name}"] = self.finance.percentage_pies[self.chart.portfolio_name-1]
        self.title_of_pie.append(f'{self.chart.portfolio_text}')

        if self.extras == "Cryptos- ESG":
            self.a.legend((f'Crypto Aggressive', f'{self.chart.selected_esg_text}', f'{self.chart.portfolio_text}'), loc='upper center', shadow=True, fontsize=15)
            self.appropriate_portfolios[f"PORTFOLIO CRYPTO: {5}"] = self.finance.percentage_pies[5]
            self.appropriate_portfolios[f"PORTFOLIO ESG: {self.chart.selected_esg+1}"] = self.finance.percentage_pies[5 + self.chart.portfolio_name]
            self.title_of_pie.append(f'Crypto Aggressive')
            self.title_of_pie.append(f"{self.chart.selected_esg_text}")

        elif self.extras == "Cryptos":
            self.a.legend((f'Crypto Aggressive', f'{self.chart.portfolio_text}'), loc='upper center', shadow=True, fontsize=15)
            self.appropriate_portfolios[f"PORTFOLIO CRYPTO: {5}"] = self.finance.percentage_pies[5]
            self.title_of_pie.append(f'Crypto Aggressive')

        elif self.extras == "ESG":
            self.a.legend((f'{self.chart.selected_esg_text}', f'{self.chart.portfolio_text}'), loc='upper center', shadow=True, fontsize=15)
            self.appropriate_portfolios[f"PORTFOLIO ESG: {self.chart.selected_esg+1}"] = self.finance.percentage_pies[5 + self.chart.portfolio_name]
            self.title_of_pie.append(f"{self.chart.selected_esg_text}")

        else:
            self.a.legend([(f'{self.chart.portfolio_text}')], loc='upper center', shadow=True, fontsize=15)

        self.create_graphs()

        self.canvas = FigureCanvasTkAgg(self.fig, master=self.root)
        self.canvas.get_tk_widget().place(x=100, y=-40)
        self.canvas.draw()

    def create_graphs(self):
        colors = {
            #                  BLUE                 GREEN
            "PORTFOLIO: 1": ['#0d0f83', '#3D3F9B', '#188300', '#40ba0f', '#66d855', '#a3ee5b', '#d1fbd8', "#DEFCE3"],
            "PORTFOLIO: 2": ['#0d0f83', '#3D3F9B', '#188300', '#40ba0f', '#66d855', '#a3ee5b', '#d1fbd8', "#DEFCE3"],
            "PORTFOLIO: 3": ['#0d0f83', '#3D3F9B', '#188300', '#40ba0f', '#66d855', '#a3ee5b', '#d1fbd8', "#DEFCE3"],
            "PORTFOLIO: 4": ['#0d0f83', '#3D3F9B', '#188300', '#40ba0f', '#66d855', '#a3ee5b', '#d1fbd8', "#DEFCE3"],
            "PORTFOLIO: 5": ['#0d0f83', '#3D3F9B', '#188300', '#40ba0f', '#66d855', '#a3ee5b', '#d1fbd8', "#DEFCE3"],
            #                        YELLOW      BLUE
            "PORTFOLIO CRYPTO: 5": ['#F6F54D', '#0d0f83', '#3D3F9B', '#6D6FB4', '#8687C1', '#9E9FCD', '#CECFE6'],
            #                       RED                  GREEN      BLUE
            "PORTFOLIO ESG: 7": ['#FD5D5D', '#FF8080', '#40ba0f', '#0d0f83', '#3D3F9B', '#6D6FB4', '#8687C1', '#9E9FCD', '#CECFE6'],
            "PORTFOLIO ESG: 8": ['#FD5D5D', '#FF8080', '#40ba0f', '#0d0f83', '#3D3F9B', '#6D6FB4', '#8687C1', '#9E9FCD', '#CECFE6'],
            "PORTFOLIO ESG: 9": ['#FD5D5D', '#FF8080', '#40ba0f', '#0d0f83', '#3D3F9B', '#6D6FB4', '#8687C1', '#9E9FCD', '#CECFE6'],
            "PORTFOLIO ESG: 10": ['#FD5D5D', '#FF8080', '#40ba0f', '#0d0f83', '#3D3F9B', '#6D6FB4', '#8687C1', '#9E9FCD', '#CECFE6'],
            #                       GREEN      BLUE
            "PORTFOLIO ESG: 11": ['#40ba0f', '#0d0f83', '#3D3F9B', '#6D6FB4', '#8687C1', '#9E9FCD', '#CECFE6'],
        }
        num = 0
        for pie in self.appropriate_portfolios:
            self.stockListExp = []
            self.stockSplitExp = []
            # explode = []
            for token in self.appropriate_portfolios[pie]:
                if self.appropriate_portfolios[pie][token] != 0:
                    self.stockListExp.append(token)
                    self.stockSplitExp.append(self.appropriate_portfolios[pie][token])

            ring = self.fig.add_subplot(self.gs[self.pies_row[num], self.pies_column[num]])
            ring.pie(self.stockSplitExp, radius=1, labels=self.stockListExp,
                     textprops={'fontsize': 16}, colors=colors[pie])
            ring.set_title(self.title_of_pie[num], fontsize=20, pad=18)  # DONUT TITLE.
            centre_circle = Circle((0, 0), 0.70, fc="white")
            ring.add_artist(centre_circle)
            num += 1

    def restart(self):
        self.a.cla()
        self.sub_btn.place_forget()
        self.container.place_forget()
        self.canvas.get_tk_widget().place_forget()
        self.total = 0
        self.question_num = 0
        self.net_worth = 0
        self.difference_money = 0
        self.risk_rate = 0
        self.extra_question = False
        self.command = ""
        self.root.configure(bg="white")
        self.chart.extras_name = []
        self.final_extra_letter = []
        self.stockListExp = []
        self.stockSplitExp = []
        self.chart.extras_chart = {}

        self.first_step()

