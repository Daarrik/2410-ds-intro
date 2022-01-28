import matplotlib.pyplot as plt
import numpy as np  # Could also just use range() wherever np.arange is used
import pandas as pd

def density_bar_graph(planet_data):
    # Part 1
    names = planet_data["Name"]         # List with only names of planets
    densities = planet_data["Density"]  # Corresponding list with only densities of planets

    plt.figure("Planet Density")
    plt.title("Planet Density")
    plt.bar(x=names,
            height=densities)               # Bar plot with bars for each planet and densities for heights
    plt.xlabel("Planet")
    plt.ylabel("Density")
    plt.xticks(rotation=-45)                # Set x-axis tick rotation
    plt.yticks(ticks=range(0, 351, 50)) # Set y-axis tick positions
    plt.show()

def rotation_pie_chart(planet_data):
    # Part 2
    rot_len = len(planet_data)                                                              # Number of planets
    pos_rot_len = len([rotation for rotation in planet_data["Rotation"] if rotation > 0])   # Number of planets with positive rotations
    pie_vals = [pos_rot_len, rot_len-pos_rot_len]                                           # [positive rotations, negative rotations]

    plt.figure("Positive Rotations vs Negative Rotations")
    plt.title("Rotations")
    plt.pie(x=pie_vals,
            labels=["Positive Rotations", "Negative Rotations"],
            autopct="%.2f%%")   # Pie plot with positive rotations and negative rotations
            # Alternatively: autopct=lambda pct : '{:.2f}%  ({:,.0f})'.format(pct,pct * sum(pie_vals)/100 
    plt.show()

def gravity_line(planet_data):
    # Part 3
    names = planet_data["Name"]
    grav = planet_data["Grav"]

    plt.figure("Planet Gravity")
    plt.title("Planet Gravity")
    plt.plot(names,grav)
    plt.xticks(rotation=-45)
    plt.yticks(ticks=np.arange(0, 81, 10))
    plt.show()

def gravity_vs_mass(planet_data):
    # Part 4
    mass = planet_data["Mass"]
    grav = planet_data["Grav"]
    labels = planet_data["Name"]
    
    plt.figure("Gravity vs. Mass")
    plt.title("Gravity vs. Mass")
    plt.scatter(mass, grav)
    for i, label in enumerate(labels):
        plt.annotate(label, (mass[i], grav[i]))
    plt.xlabel("Mass")
    plt.ylabel("Gravity")
    plt.show()

def main():
    planet_data = pd.read_csv("C:/Users/Darrik/Documents/Python/2410/Assignment 2/planets.csv")

    # Part 1
    # Open planet density bar graph
    density_bar_graph(planet_data)

    # Part 2
    # Open rotation percentage pie chart
    rotation_pie_chart(planet_data)

    # Part 3
    # Open multiple line graph
    gravity_line(planet_data)

    # Part 4
    # My own plot
    gravity_vs_mass(planet_data)

if __name__ == "__main__":
    main()