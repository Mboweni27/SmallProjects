from scipy.stats import binom
import numpy as np
import random
from tabulate import tabulate
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

def probability_of_trades():
    numberoftrades = 8
    probability = 0.5
    x = np.arange(0, numberoftrades + 1)
    probabilities = binom.pmf(x, numberoftrades, probability)
    for i in range(len(x)):
        print(f"Number of wins: ", x[i], " out of ", numberoftrades ,"Probability: ", round(probabilities[i]*100,2),"%")

"This was with 160 Trades"
def first_month():
    number_of_wins = 0
    number_of_loses = 0
    starting_capital = 25000 #prop firm
    goal =1250
    max_loss = -1250
    num_of_trades = 160
    PNL = 0
    trade_counter = 1
    challenge_passed = False
    
    while trade_counter <= num_of_trades:
        profit_per_trade = random.randint(68,95)
        loss_per_trade = random.randint(35,75)
        random_trade = random.randint(0,1)
        if(random_trade == 1):
            PNL += profit_per_trade
            number_of_wins+=1
    
        elif(random_trade == 0):
            PNL -= loss_per_trade
            number_of_loses+=1
    
        if not challenge_passed and PNL >= goal:
            print("✅ Challenge PASSED")
            print("(Goal of $1250) You have successfuly passed this futures challenge in", trade_counter," trades")
            print("Wins:", number_of_wins)
            print("Losses:", number_of_loses)
            number_of_days = round(trade_counter/8,2)
            print("This translates to about:",number_of_days, "days\n")
            challenge_passed = True
            number_of_wins = 0
            number_of_loses = 0
            starting_capital = 25000
            PNL = 0
        if not challenge_passed and PNL <= max_loss:
            print("❌ Challenge FAILED")
            print("You have failed this futures challenge ", trade_counter, " trades")
            print("Wins:", number_of_wins)
            print("Losses:", number_of_loses)
            number_of_days = round(trade_counter/8,2)
            print("This translates to about:",number_of_days, "days\n")
            challenge_passed = False
            number_of_wins = 0
            number_of_loses = 0
            starting_capital = 25000
            PNL = 0
        trade_counter+=1
    
    print("\n📊 Funded Account")
    '''RED = "\033[91m"
    GREEN = "\033[92m"
    BLUE = "\033[94m"
    '''
    days_in_funded = number_of_wins + number_of_loses
    data = [
    
        ["Wins", number_of_wins],
        ["Losses",number_of_loses],
        ["Days",round(days_in_funded/8,2)],
        ["PNL", f"${round(PNL,2)}"],
        ["Account",f"${round(starting_capital+PNL,2)}"]
     
    ]
    print(tabulate(data, headers = ["Metric", "Value"], tablefmt="fancy_grid",  colalign=["left", "left"]))
    '''brave_path = "C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"
    chrome_options = Options()
    chrome_options.binary_location = brave_path
    service = Service("C:\\Cool Hacking Stuff 2\\chromedriver-win64\\chromedriver.exe")  # Make sure this matches your downloaded ChromeDriver
    driver = webdriver.Chrome(service=service, options=chrome_options)
    url = "https://www.google.com/search?q=dollar+to+rand&oq=dollar+to+rand&gs_lcrp=EgZjaHJvbWUyBggAEEUYOTIGCAEQLhhA0gEINTExOWowajGoAgCwAgA&sourceid=chrome&ie=UTF-8"
    driver.get(url)
    time.sleep(1.5)
    driver.find_element_by_xpath('//input[contains(@class, "lWzCpb")]')
    driver.get_attribute("value")
    '''
    rand_value = PNL * 18.62
    print(f"🇿🇦 Estimated Rand Earnings:\nR{rand_value:,.2f}\n")


"This was with 160 Trades"
def months_after():
    wins = 0
    losses = 0
    capital= 25000
    trades = 160
    PNL = 0
    trade_counter = 0
    while trade_counter < 160:
        trade_take = random.randint(0,1)
        profit_per_trade = random.randint(68,95)
        loss_per_trade = random.randint(35,75)
        if trade_take == 1:
            PNL += profit_per_trade
            wins+=1

        elif trade_take == 0:
            PNL -= loss_per_trade
            losses += 1
        trade_counter+=1


    print("📊 New_Month_Prediction")
    data = [
        ["Wins", wins],
        ["Losses", losses],
        ["PNL", f"${round(PNL,2)}"],
        ["Account",f"${round(capital+PNL,2)}"]
     
    ]
    print(tabulate(data, headers = ["Metric", "Value"], tablefmt="fancy_grid",  colalign=["left", "left"]))
    rand_value = PNL * 18.62
    print(f"🇿🇦 Estimated Rand Earnings:\nR{rand_value:,.2f}\n")


def day_trading():
    profit_goal = 180
    max_loss = -150
    wins = 0
    losses = 0
    PNL = 0
    trade_counter = 0
    while trade_counter < 8:
        win_or_loss = random.randint(0, 1)
        amount_won = random.randint(70, 97)
        amount_loss = random.randint(25, 90)
        if(win_or_loss == 1):
            PNL += amount_won
            wins += 1
            if(PNL >= profit_goal):
                #this is temporary
                PNL = 180
                print("✅Profit target for day reached")
                print("......📊Results......")
                data = [
                    ["Wins", wins],
                    ["Losses", losses],
                    ["PNL", f"${round(PNL,2)}"]
                ]
                print(tabulate(data, headers = ["Metric", "Value"], tablefmt="fancy_grid",  colalign=["left", "left"]))
                rand_value = PNL * 18.62
                print(f"🇿🇦 Estimated Rand Earnings:\nR{rand_value:,.2f}\n")
                break
        elif(win_or_loss == 0):
            PNL-=amount_loss
            losses +=1
            if(PNL <= max_loss):
                #this is temporary
                PNL = -150
                print("❌ Max loss for the day reached")
                print("......📊Results......")
                data = [
                    ["Wins", wins],
                    ["Losses", losses],
                    ["PNL", f"${round(PNL,2)}"]
                ]  
                print(tabulate(data, headers = ["Metric", "Value"], tablefmt="fancy_grid",  colalign=["left", "left"]))
                rand_value = PNL * 18.62
                print(f"🇿🇦 Estimated Rand Earnings:\nR{rand_value:,.2f}\n")  
                break
        trade_counter+=1
    else:
        print("🔚Day ended without hitting target or max loss.")
        print("......📊Results......")
        data = [
            ["Wins", wins],
            ["Losses", losses],
            ["PNL", f"${round(PNL,2)}"]
        ]  
        print(tabulate(data, headers = ["Metric", "Value"], tablefmt="fancy_grid",  colalign=["left", "left"]))
        rand_value = PNL * 18.62
        print(f"🇿🇦 Estimated Rand Earnings:\nR{rand_value:,.2f}\n")
    return PNL, wins, losses

def first_month_prop_firm():
    eval_wins = 0
    eval_losses = 0
    eval_PNL = 0
    goal = 1250
    max_loss = -1250
    starting_capital = 25000
    challenge_passed = False
    print("📈 First Months Eval Account Prediction")
    for day in range(1,21):
        PNL, wins, losses = day_trading()
        eval_PNL += PNL
        eval_wins += wins
        eval_losses += losses
        if not challenge_passed and eval_PNL >= goal:
            print("✅ Challenge PASSED")
            print("(Goal of $1250) You have successfuly passed this futures challenge in", eval_wins + eval_losses," trades")
            print("Wins:", eval_wins)
            print("Losses:", eval_losses)
            print("This translates to about:", day, "days\n")
            print("PNL:", eval_PNL)
            challenge_passed = True
            eval_wins = 0
            eval_losses = 0
            starting_capital = 25000
            return

        if not challenge_passed and PNL <= max_loss:
            print("❌ Challenge FAILED")
            print("You have failed this futures challenge ", eval_wins + eval_losses, " trades")
            print("Wins:", eval_wins)
            print("Losses:", eval_losses)
            print("This translates to about:",day, "days\n")
            print("PNL:", eval_PNL)
            challenge_passed = False
            eval_wins = 0
            eval_losses = 0
            starting_capital = 25000
            return

def week_trading():
    weekly_PNL = 0
    weekly_wins = 0
    weekly_losses = 0
    print("📈 Weekly Trading Simulation")
    for day in range(1,6):
        PNL, wins, losses = day_trading()
        weekly_PNL += PNL
        weekly_wins += wins
        weekly_losses += losses
    print("🧾Final Weekly Summary")

    weekly_data = [
        ["Total Wins", weekly_wins],
        ["Total Losses", weekly_losses],
        ["Total Trades", weekly_wins+weekly_losses],
        ["Winrate", (weekly_wins/(weekly_wins+weekly_losses))*100],
        ["Total PNL", f"${weekly_PNL:.2f}"],

    ]
    print(tabulate(weekly_data, headers = ["Metric", "Value"], tablefmt="fancy_grid",  colalign=["left", "left"]))
    rand_value = weekly_PNL * 18.62
    print(f"🇿🇦 Estimated Rand Earnings:\nR{rand_value:,.2f}\n")

def month_trading_parameters():
    monthly_PNL = 0
    monthly_wins = 0
    monthly_losses= 0 
    print("📈Monthly Trading Simulation")
    for month in range(1,21):
        PNL, wins, losses = day_trading()
        monthly_wins += wins
        monthly_losses += losses
        monthly_trades = monthly_wins + monthly_losses
        monthly_PNL += PNL
    print("🧾Final Monthy Summary")

    monthly_data = [
        ["Total Wins", monthly_wins],
        ["Total Losses", monthly_losses],
        ["Total Trades", monthly_trades],
        ["Winrate", (monthly_wins/(monthly_wins+monthly_losses))*100],
        ["Total PNL", f"${monthly_PNL:.2f}"],

    ]
    print(tabulate(monthly_data, headers = ["Metric", "Value"], tablefmt="fancy_grid",  colalign=["left", "left"]))
    rand_value = monthly_PNL * 18.62
    print(f"🇿🇦 Estimated Rand Earnings:\nR{rand_value:,.2f}\n")




'''
NOW IMA DO DOUBLE OF EVERYTHING
'''

def double_first_month():
    number_of_wins = 0
    number_of_loses = 0
    starting_capital = 50000 #prop firm
    goal =2500
    max_loss = -2500
    num_of_trades = 160
    PNL = 0
    trade_counter = 1
    challenge_passed = False
    
    while trade_counter <= num_of_trades:
        profit_per_trade = random.randint(136,190)
        loss_per_trade = random.randint(70,150)
        random_trade = random.randint(0,1)
        if(random_trade == 1):
            PNL += profit_per_trade
            number_of_wins+=1
    
        elif(random_trade == 0):
            PNL -= loss_per_trade
            number_of_loses+=1
    
        if not challenge_passed and PNL >= goal:
            print("✅ Challenge PASSED")
            print("(Goal of $2500)You have successfuly passed this futures challenge in", trade_counter," trades")
            print("Wins:", number_of_wins)
            print("Losses:", number_of_loses)
            number_of_days = round(trade_counter/8,2)
            print("This translates to about:",number_of_days, "days\n")
            challenge_passed = True
            number_of_wins = 0
            number_of_loses = 0
            starting_capital = 50000
            PNL = 0
        if not challenge_passed and PNL <= max_loss:
            print("❌ Challenge FAILED")
            print("You have failed this futures challenge ", trade_counter, " trades")
            print("Wins:", number_of_wins)
            print("Losses:", number_of_loses)
            number_of_days = round(trade_counter/8,2)
            print("This translates to about:",number_of_days, "days\n")
            challenge_passed = False
            number_of_wins = 0
            number_of_loses = 0
            starting_capital = 50000
            PNL = 0
        trade_counter+=1
    
    print("\n📊 Funded Account")
    '''RED = "\033[91m"
    GREEN = "\033[92m"
    BLUE = "\033[94m"
    '''
    days_in_funded = number_of_wins + number_of_loses
    data = [
    
        ["Wins", number_of_wins],
        ["Losses",number_of_loses],
        ["Days",round(days_in_funded/8,2)],
        ["PNL", f"${round(PNL,2)}"],
        ["Account",f"${round(starting_capital+PNL,2)}"]
     
    ]
    print(tabulate(data, headers = ["Metric", "Value"], tablefmt="fancy_grid",  colalign=["left", "left"]))
    '''brave_path = "C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"
    chrome_options = Options()
    chrome_options.binary_location = brave_path
    service = Service("C:\\Cool Hacking Stuff 2\\chromedriver-win64\\chromedriver.exe")  # Make sure this matches your downloaded ChromeDriver
    driver = webdriver.Chrome(service=service, options=chrome_options)
    url = "https://www.google.com/search?q=dollar+to+rand&oq=dollar+to+rand&gs_lcrp=EgZjaHJvbWUyBggAEEUYOTIGCAEQLhhA0gEINTExOWowajGoAgCwAgA&sourceid=chrome&ie=UTF-8"
    driver.get(url)
    time.sleep(1.5)
    driver.find_element_by_xpath('//input[contains(@class, "lWzCpb")]')
    driver.get_attribute("value")
    '''
    rand_value = PNL * 18.62
    print(f"🇿🇦 Estimated Rand Earnings:\nR{rand_value:,.2f}\n")

def double_months_after():
    wins = 0
    losses = 0
    capital= 50000
    trades = 160
    PNL = 0
    trade_counter = 0
    while trade_counter < 160:
        trade_take = random.randint(0,1)
        profit_per_trade = random.randint(136,190)
        loss_per_trade = random.randint(70,150)
        if trade_take == 1:
            PNL += profit_per_trade
            wins+=1

        elif trade_take == 0:
            PNL -= loss_per_trade
            losses += 1
        trade_counter+=1


    print("📊 New_Month_Prediction")
    data = [
        ["Wins", wins],
        ["Losses", losses],
        ["PNL", f"${round(PNL,2)}"],
        ["Account",f"${round(capital+PNL,2)}"]
     
    ]
    print(tabulate(data, headers = ["Metric", "Value"], tablefmt="fancy_grid",  colalign=["left", "left"]))
    rand_value = PNL * 18.62
    print(f"🇿🇦 Estimated Rand Earnings:\nR{rand_value:,.2f}\n")
    
def double_day_trading():
    profit_goal = 360
    max_loss = -300
    wins = 0
    losses = 0
    PNL = 0
    trade_counter = 0
    while trade_counter < 8:
        win_or_loss = random.randint(0, 1)
        amount_won = random.randint(136, 190)
        amount_loss = random.randint(70, 150)
        if(win_or_loss == 1):
            PNL += amount_won
            wins += 1
            if(PNL >= profit_goal):
                #temp
                PNL = 360
                print("✅Profit target for day reached")
                print("......📊Results......")
                data = [
                    ["Wins", wins],
                    ["Losses", losses],
                    ["PNL", f"${round(PNL,2)}"]
                ]
                print(tabulate(data, headers = ["Metric", "Value"], tablefmt="fancy_grid",  colalign=["left", "left"]))
                rand_value = PNL * 18.62
                print(f"🇿🇦 Estimated Rand Earnings:\nR{rand_value:,.2f}\n")
                break
        elif(win_or_loss == 0):
            PNL-=amount_loss
            losses +=1
            if(PNL <= max_loss):
                #temp
                PNL = -260
                print("❌ Max loss for the day reached")
                print("......📊Results......")
                data = [
                    ["Wins", wins],
                    ["Losses", losses],
                    ["PNL", f"${round(PNL,2)}"]
                ]  
                print(tabulate(data, headers = ["Metric", "Value"], tablefmt="fancy_grid",  colalign=["left", "left"]))
                rand_value = PNL * 18.62
                print(f"🇿🇦 Estimated Rand Earnings:\nR{rand_value:,.2f}\n")  
                break
        trade_counter+=1
    else:
        print("🔚Day ended without hitting target or max loss.")
        print("......📊Results......")
        data = [
            ["Wins", wins],
            ["Losses", losses],
            ["PNL", f"${round(PNL,2)}"]
        ]  
        print(tabulate(data, headers = ["Metric", "Value"], tablefmt="fancy_grid",  colalign=["left", "left"]))
        rand_value = PNL * 18.62
        print(f"🇿🇦 Estimated Rand Earnings:\nR{rand_value:,.2f}\n")
    return PNL, wins, losses

def double_week_trading():
    weekly_PNL = 0
    weekly_wins = 0
    weekly_losses = 0
    print("📈 Weekly Trading Simulation")
    for day in range(1,6):
        PNL, wins, losses = double_day_trading()
        weekly_PNL += PNL
        weekly_wins += wins
        weekly_losses += losses
    print("🧾Final Weekly Summary")
    weekly_data = [
        ["Total Wins", weekly_wins],
        ["Total Losses", weekly_losses],
        ["Total Trades", weekly_wins+weekly_losses],
        ["Winrate", (weekly_wins/(weekly_wins+weekly_losses))*100],
        ["Total PNL", f"${weekly_PNL:.2f}"],
    ]
    print(tabulate(weekly_data, headers = ["Metric", "Value"], tablefmt="fancy_grid",  colalign=["left", "left"]))
    rand_value = weekly_PNL * 18.62
    print(f"🇿🇦 Estimated Rand Earnings:\nR{rand_value:,.2f}\n")

def double_month_trading_parameters():
    monthly_PNL = 0
    monthly_wins = 0
    monthly_losses= 0 
    print("📈Monthly Trading Simulation")
    for month in range(1,21):
        PNL, wins, losses = double_day_trading()
        monthly_wins += wins
        monthly_losses += losses
        monthly_PNL += PNL
    print("🧾Final Monthy Summary")

    monthly_data = [
        ["Total Wins", monthly_wins],
        ["Total Losses", monthly_losses],
        ["Winrate", (monthly_wins/(monthly_wins+monthly_losses))*100],
        ["Total PNL", f"${monthly_PNL:.2f}"],

    ]
    print(tabulate(monthly_data, headers = ["Metric", "Value"], tablefmt="fancy_grid",  colalign=["left", "left"]))
    rand_value = monthly_PNL * 18.62
    print(f"🇿🇦 Estimated Rand Earnings:\nR{rand_value:,.2f}\n")




def day_trading_100k():
    profit_goal = 720
    max_loss = -600
    wins = 0
    losses = 0
    PNL = 0
    trade_counter = 0
    while trade_counter < 8:
        win_or_loss = random.randint(0, 1)
        amount_won = random.randint(272, 380)
        amount_loss = random.randint(140, 300)
        if(win_or_loss == 1):
            PNL += amount_won
            wins += 1
            if(PNL >= profit_goal):
                PNL = 720
                print("✅Profit target for day reached")
                print("......📊Results......")
                data = [
                    ["Wins", wins],
                    ["Losses", losses],
                    ["PNL", f"${round(PNL,2)}"]
                ]
                print(tabulate(data, headers = ["Metric", "Value"], tablefmt="fancy_grid",  colalign=["left", "left"]))
                rand_value = PNL * 18.62
                print(f"🇿🇦 Estimated Rand Earnings:\nR{rand_value:,.2f}\n")
                break
        elif(win_or_loss == 0):
            PNL-=amount_loss
            losses +=1
            if(PNL <= max_loss):
                PNL= -600
                print("❌ Max loss for the day reached")
                print("......📊Results......")
                data = [
                    ["Wins", wins],
                    ["Losses", losses],
                    ["PNL", f"${round(PNL,2)}"]
                ]  
                print(tabulate(data, headers = ["Metric", "Value"], tablefmt="fancy_grid",  colalign=["left", "left"]))
                rand_value = PNL * 18.62
                print(f"🇿🇦 Estimated Rand Earnings:\nR{rand_value:,.2f}\n")  
                break
        trade_counter+=1
    else:
        print("🔚Day ended without hitting target or max loss.")
        print("......📊Results......")
        data = [
            ["Wins", wins],
            ["Losses", losses],
            ["PNL", f"${round(PNL,2)}"]
        ]  
        print(tabulate(data, headers = ["Metric", "Value"], tablefmt="fancy_grid",  colalign=["left", "left"]))
        rand_value = PNL * 18.62
        print(f"🇿🇦 Estimated Rand Earnings:\nR{rand_value:,.2f}\n")
    return PNL, wins, losses

def week_trading_100k():
    weekly_PNL_100k = 0
    weekly_wins_100k = 0
    weekly_losses_100k = 0
    print("📈 Weekly Trading Simulation")
    for day in range(1,6):
        PNL, wins, losses = day_trading_100k()
        weekly_PNL_100k += PNL
        weekly_wins_100k += wins
        weekly_losses_100k += losses
    print("🧾Final Weekly Summary")
    weekly_data_100k = [
        ["Total Wins", weekly_wins_100k],
        ["Total Losses", weekly_losses_100k],
        ["Total Trades", weekly_wins_100k+weekly_losses_100k],
        ["Winrate", (weekly_wins_100k/(weekly_wins_100k+weekly_losses_100k))*100],
        ["Total PNL", f"${weekly_PNL_100k:.2f}"],
    ]
    print(tabulate(weekly_data_100k, headers = ["Metric", "Value"], tablefmt="fancy_grid",  colalign=["left", "left"]))
    rand_value = weekly_PNL_100k * 18.62
    print(f"🇿🇦 Estimated Rand Earnings:\nR{rand_value:,.2f}\n")

def month_trading_100K():
    monthly_PNL = 0
    monthly_wins = 0
    monthly_losses= 0 
    print("📈Monthly Trading Simulation")
    for month in range(1,21):
        PNL, wins, losses = day_trading_100k()
        monthly_wins += wins
        monthly_losses += losses
        monthly_PNL += PNL
    print("🧾Final Monthy Summary")

    monthly_data = [
        ["Total Wins", monthly_wins],
        ["Total Losses", monthly_losses],
        ["Winrate", (monthly_wins/(monthly_wins+monthly_losses))*100],
        ["Total PNL", f"${monthly_PNL:.2f}"],

    ]
    print(tabulate(monthly_data, headers = ["Metric", "Value"], tablefmt="fancy_grid",  colalign=["left", "left"]))
    rand_value = monthly_PNL * 18.62
    print(f"🇿🇦 Estimated Rand Earnings:\nR{rand_value:,.2f}\n")

def Account_100k():
    monthly_PNL = 0
    monthly_wins = 0
    monthly_losses= 0 
    print("📈Monthly Trading Simulation")
    for month in range(1,21):
        PNL, wins, losses = day_trading_100k()
        monthly_wins += wins
        monthly_losses += losses
        monthly_PNL += PNL
    print("🧾Final Monthy Summary")

    monthly_data = [
        ["Total Wins", monthly_wins],
        ["Total Losses", monthly_losses],
        ["Winrate", (monthly_wins/(monthly_wins+monthly_losses))*100],
        ["Total PNL", f"${monthly_PNL:.2f}"],

    ]
    print(tabulate(monthly_data, headers = ["Metric", "Value"], tablefmt="fancy_grid",  colalign=["left", "left"]))
    rand_value = monthly_PNL * 18.62
    print(f"🇿🇦 Estimated Rand Earnings:\nR{rand_value:,.2f}\n")




'''MAIN'''

#probability_of_trades()

#first_month()
#double_first_month()

#months_after()
#double_months_after()

#day_trading()
#double_day_trading()
#first_month_prop_firm()
#week_trading()
#double_week_trading()


month_trading_parameters()
#double_month_trading_parameters()

#week_trading_100k()
#Account_100k()
#month_trading_100K()

#month_after_100k()





'''okay now ima generate a while loop that 
will keep going until i see one month with a 21% winrate
'''


