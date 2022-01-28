import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("tennis.csv", encoding="latin1", nrows=90)

print(data["WINNER"])