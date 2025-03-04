from replit import clear
import csv
import yfinance as yf
import pandas as pd

def load_portfolio(filename="portfolio.csv"):
    try:
        with open(filename, mode='r') as file:
            reader = csv.reader(file)
            return [row for row in reader]
    except FileNotFoundError:
        return []

def save_portfolio(portfolio, filename="portfolio.csv"):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(portfolio)

def add_stock(symbol, quantity, portfolio):
    portfolio.append([symbol.upper(), quantity])
    save_portfolio(portfolio)
    print(f"Added {quantity} shares of {symbol.upper()} to portfolio.")

def remove_stock(symbol, portfolio):
    portfolio = [stock for stock in portfolio if stock[0] != symbol.upper()]
    save_portfolio(portfolio)
    print(f"Removed {symbol.upper()} from portfolio.")
    return portfolio

def get_stock_price(symbol):
    stock = yf.Ticker(symbol)
    price = stock.history(period="1d").Close[-1]
    return round(price, 2)

def view_portfolio(portfolio):
    #print("\nYour Stock Portfolio:")
    #filePath = 'portfolio.csv'
    #data = pd.read_csv(filePath)
    #data.info()
    for stock in portfolio:
        symbol, quantity = stock
        try:
            price = get_stock_price(symbol)
            value = price * int(quantity)
            print(f"{symbol}: {quantity} shares @ ${price} each = ${value}")
        except:
            print(f"{symbol}: {quantity} shares (Price unavailable)")

# Example usage
portfolio = load_portfolio()
while True:
    print("\nStock Portfolio Tracker")
    print("1. Add Stock")
    print("2. Remove Stock")
    print("3. View Portfolio")
    print("4. Exit")
    choice = input("Choose an option: ")
    clear()
    
    if choice == "1":
        symbol = input("Enter stock symbol: ")
        quantity = input("Enter quantity: ")
        add_stock(symbol, quantity, portfolio)
    elif choice == "2":
        symbol = input("Enter stock symbol to remove: ")
        portfolio = remove_stock(symbol, portfolio)
    elif choice == "3":
        view_portfolio(portfolio)
    elif choice == "4":
        break
    else:
        print("Invalid option, please try again.")