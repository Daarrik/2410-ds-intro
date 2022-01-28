# Group 6: Darrik Houck, Celine Mangahas

import csv
import matplotlib.pyplot as plt

# Read all data
data = []
with open("tennis.csv") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        if int(row["YEAR"]) < 2000:
            break
        year = int(row["YEAR"])
        trny = row["TOURNAMENT"]
        winner = row["WINNER"]
        runner_up = row["RUNNER-UP"]

        data.append({"Year": year, "Tournament": trny, "Winner": winner, "RunnerUp": runner_up})

# Major winners: 2000-2021
winners = {}
for entry in data:
    if entry["Winner"] not in winners:
        winners[entry["Winner"]] = 1
    else:
        winners[entry["Winner"]] += 1

# Major runners-up: 2000-2021
runnersup = {}
for entry in data:   
    if entry["RunnerUp"] not in runnersup:
        runnersup[entry["RunnerUp"]] = 1
    else:
        runnersup[entry["RunnerUp"]] += 1

# Major winners' number of losses in major finals
winner_final_loss = {}
for player in winners.keys():
    if player in runnersup:
        winner_final_loss[player] = runnersup[player]
    else:
        winner_final_loss[player] = 0

# Major winners and number of final losses
plt.title("Major Winners: 2000 to 2021")
plt.barh(y=list(winners.keys())[::-1],
        width=list(winners.values())[::-1],
        label="Major Wins",
        height=.4,
        align="edge",
        color="steelblue",
        zorder=3)
plt.barh(y=list(winner_final_loss.keys())[::-1],
        width=list(winner_final_loss.values())[::-1],
        height=-.4,
        label="Major Runner-Up",
        align="edge",
        color="indianred",
        zorder=3)
plt.legend()
plt.grid(axis="x",
         zorder=0)
plt.xlabel("Number of Majors")
plt.xticks(range(0, 21))
plt.show()

# Big 3 major wins percentage: 2000-2021
# Big 3 = Novak Djokovic, Roger Federer, Rafael Nadal
big_3_wins = winners["Novak Djokovic"] + winners["Rafael Nadal"] + winners["Roger Federer"]
non_big_3_wins = sum(winners.values()) - big_3_wins

plt.title("Big 3 Major Win Percentage: 2000 to 2021")
plt.pie(x=[big_3_wins, non_big_3_wins],
        labels=["Big 3 Wins", "Everyone else"],
        colors=["steelblue", "lightgray"],
        startangle=90,
        autopct="%.2f%%")
plt.show()

# Big 3 title accumulation
def year_dictionary():
    years = {}
    for i in range(2000, 2022):
        years[i] = 0
    return years

djoko = year_dictionary()
fed = year_dictionary()
nadal = year_dictionary()
years = range(2000, 2022)

# Djokovic major history
for entry in data:
    if entry["Winner"] == "Novak Djokovic":
        djoko[entry["Year"]] += 1
        for year in djoko.keys():
            if year > entry["Year"]:
                djoko[year] += 1


# Federer major history
for entry in data:
    if entry["Winner"] == "Roger Federer":
        fed[entry["Year"]] += 1
        for year in fed.keys():
            if year > entry["Year"]:
                fed[year] += 1

# Nadal major history
for entry in data:
    if entry["Winner"] == "Rafael Nadal":
        nadal[entry["Year"]] += 1
        for year in nadal.keys():
            if year > entry["Year"]:
                nadal[year] += 1


# Big 3 Major History
plt.title("Major History of the Big 3")
plt.plot(range(0, 22), djoko.values(), color="steelblue")
plt.plot(range(0, 22), fed.values(), color="lightgreen")
plt.plot(range(0, 22), nadal.values(), color="indianred")
plt.legend(["Novak Djokovic", "Roger Federer", "Rafael Nadal"])
plt.xlabel("Year")
plt.ylabel("Accumulative Major Titles")
plt.xticks(ticks=range(0, 22), labels=years)
plt.yticks(range(0, 21))
plt.show()

# Big 3 Major Final Win/Loss percentage
# ax1 = Djokovic, ax2 = Federer, ax3 = Nadal
fig, (ax1, ax2, ax3) = plt.subplots(1, 3)
plt.suptitle("Big 3 Major Final Win/Loss Rate")
ax1.set_title("Novak Djokovic")
ax1.pie([winners["Novak Djokovic"], runnersup["Novak Djokovic"]],
        labels=["Wins", "Losses"],
        colors=["steelblue", "indianred"],
        autopct="%.2f%%")
ax2.set_title("Roger Federer")
ax2.pie([winners["Roger Federer"], runnersup["Roger Federer"]],
        labels=["Wins", "Losses"],
        colors=["steelblue", "indianred"],
        autopct="%.2f%%")
ax3.set_title("Rafael Nadal")
ax3.pie([winners["Rafael Nadal"], runnersup["Rafael Nadal"]],
        labels=["Wins", "Losses"],
        colors=["steelblue", "indianred"],
        autopct="%.2f%%")
plt.show()

# Which major has the most first time winners: 2000-2021
trny_first_time_winners = {"Australian Open": 0,
                           "French Open": 0,
                           "Wimbledon": 0,
                           "U.S. Open": 0}

# These players had already won a Major before 2000, not first timers.
appeared_players = ["Pete Sampras", "Gustavo Kuerten", "Andre Agassi"]
for entry in data[::-1]:
    if entry["Winner"] not in appeared_players:
        appeared_players.append(entry["Winner"])
        trny_first_time_winners[entry["Tournament"]] += 1

plt.title("Number of First Time Winners at Majors: 2000 to 2021")
plt.bar(x=list(trny_first_time_winners.keys()),
        height=trny_first_time_winners.values(),
        color="steelblue",
        zorder=3)
plt.grid(axis="y",
        zorder=0)
plt.show()