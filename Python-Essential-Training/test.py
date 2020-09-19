import pandas as pd


data = pd.read_csv("D:\\docker\\test-folder\\aaa\\nba.csv", index_col="Name")

# retrieving row by loc method
first = data.loc["a"]
second = data.loc["b"]

print(first, "\n\n\n", second)