# Stock Portfolio Tracker

stocks = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 150,
    "MSFT": 300,
    "AMZN": 200
}

total_investment = 0

print("=== Stock Portfolio Tracker ===")

while True:
    stock_name = input("\nEnter Stock Name (or 'done' to finish): ").upper()

    if stock_name == "DONE":
        break

    if stock_name in stocks:
        quantity = int(input("Enter Quantity: "))

        investment = stocks[stock_name] * quantity
        total_investment += investment

        print(f"{stock_name} Price: ${stocks[stock_name]}")
        print(f"Investment Value: ${investment}")

    else:
        print("Stock not found! Available stocks:")
        print(", ".join(stocks.keys()))

print("\n===== Portfolio Summary =====")
print(f"Total Investment Value: ${total_investment}")

# Save result in text file
with open("portfolio.txt", "w") as file:
    file.write("Stock Portfolio Tracker\n")
    file.write(f"Total Investment Value: ${total_investment}")

print("Portfolio saved to portfolio.txt")