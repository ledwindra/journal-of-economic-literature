import matplotlib.pyplot as plt
import numpy as np

def highest_jel(df, jel: str):
    fig, ax = plt.subplots(figsize=(20, 5))
    plt.plot("year", "count", data=df, color="black")
    plt.title(f"JEL Classification Code: {jel}")
    plt.xlabel("Year")
    plt.ylabel("Count")
    plt.xticks(np.arange(df.year.min(), df.year.max()+1, 1), rotation=45)
    ax.grid(True, linewidth=1, alpha=0.25)
    plt.show

def top_five_jel(df, column="jel", journal_name="Overall", y_interval=10):
    top_five = df.groupby(column).size().to_frame().reset_index().sort_values(by=0, ascending=False)
    top_five = top_five.reset_index(drop=True)[:5][column].to_list()
    df = df[df[column].isin(top_five)]
    dfs = [df[df[column] == x].groupby("year").size() for x in top_five]
    dfs = [x.to_frame().reset_index().rename(columns={0: "count"}) for x in dfs]
    ymax = max([x["count"].max() for x in dfs])

    # visualize
    fig, ax = plt.subplots(figsize=(20, 5))
    plt.plot("year", "count", data=dfs[0], color="black")
    plt.plot("year", "count", "--", data=dfs[1], color="red")
    plt.plot("year", "count", ":", data=dfs[2], color="blue")
    plt.plot("year", "count", "-.", data=dfs[3], color="green")
    plt.plot("year", "count", "", data=dfs[4], color="orange")
    plt.title(f"Top five JEL classification codes: {journal_name}")
    plt.xlabel("Year")
    plt.ylabel("Count")
    plt.xticks(np.arange(df.year.min(), df.year.max()+1, 1), rotation=45)
    plt.yticks(np.arange(0, ymax+1, y_interval))
    ax.legend(labels=top_five, loc="best")
    ax.grid(True, linewidth=1, alpha=0.25)
    plt.show()