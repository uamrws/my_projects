import numpy as np
import pandas as pd
import os
import matplotlib.pyplot as plt


def klines():
    names = [
        'open_time',
        'open',
        'high',
        'low',
        'close',
        'volume',
        'close_time',
        'quote_asset_volume',
        'number_of_trades',
        'taker_buy_base_asset_volume',
        'taker_buy_quote_asset_volume',
        'ignore'
    ]
    dfs = []
    for i in os.listdir("data"):
        dfs.append(
            pd.read_csv(
                os.path.join("data", i),
                header=None,
                names=names,
                usecols=["close"]
            )
        )
    df = pd.concat(dfs, ignore_index=True)
    # df = df[df["isBuyerMaker"]]
    # df = df[["price", "qty"]]
    df.insert(df.shape[1], 'count', 0)

    df = df.groupby("close").count()
    df = df[df["count"] > 10]
    print(df)

    ax = df.plot.bar(figsize=(25, 6))
    for x, y in enumerate(df['count']):
        ax.text(x, y + 0.05, y, ha='center', va='bottom', fontsize=10)

    plt.show()


def trades():
    names = ["trade_id", "price", "qty", "quoteQty", "time", "isBuyerMaker", "isBestMatch"]
    dfs = []
    for i in os.listdir("data"):
        dfs.append(
            pd.read_csv(
                os.path.join("data", i),
                header=None,
                names=names,
                usecols=["price", "qty"]
            )
        )
    df = pd.concat(dfs, ignore_index=True)
    # df = df[df["isBuyerMaker"]]
    df = df[["price", "qty"]]

    df = df.groupby("price").sum()
    df.sort_values("qty")

    ax = df.plot.bar(figsize=(25, 6))
    for x, y in enumerate(df['count']):
        ax.text(x, y + 0.05, y, ha='center', va='bottom', fontsize=10)

    plt.show()


def main():
    klines()
    # trades()


if __name__ == '__main__':
    main()
