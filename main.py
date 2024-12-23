print("Hello - SIG Winter Break 2024-2025 Dual Arbitrage project")
print("Main Github Link: ")


from src.intake.load_data import load_data
# from src.model.model import train_model
# from src.execution.run import save_results



def main():
    symbols_to_fetch = ["BRK-A","BRK-B"]
    interval = "1m"
    period = "1d"

    data = load_data(symbols_to_fetch,interval, period)

    for symbol, df in data.items():
        print(df.head())
        print(df["Ask"] - df["Bid"]) # just seeing it works in this line - has no value


if __name__ == "__main__":
    main()