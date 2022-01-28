import csv
import matplotlib.pyplot as plt
import numpy as np  # Could also just use range() where np.arange is used

def plots(planet_data):
    names = [planet["Name"] for planet in planet_data]      # List with only names of planets
    densities = [planet["Dens"] for planet in planet_data]  # Corresponding list with only densities of planets

    fig, (ax1, ax2) = plt.subplots(2, 1)                    # Two axes, one figure (window)
    ax1.bar(x=names,
            height=densities)                               # ax1 = bar plot with bars for each planet and densities for heights
    ax1.set_title("Planet Density")
    ax1.set_xlabel("Planet")
    ax1.set_ylabel("Density")
    ax1.set_xticks(ticks=np.arange(0, 9, 1))                # Set ax1 x-axis tick positions
    ax1.set_xticklabels(labels=names, rotation=-45)         # Set ax1 x-axis tick labels, text rotation
    ax1.set_yticks(ticks=np.arange(0, 351, 50))             # Set ax1 y-axis tick positions

    rot_len = len(planet_data)                                                          # Number of planets
    pos_rot_len = len([planet["Rot"] for planet in planet_data if planet["Rot"] > 0])   # Number of planets with positive rotations
    pie_vals = [pos_rot_len, rot_len-pos_rot_len]                                       # [positive rotations, negative rotations]
    
    ax2.pie(x=pie_vals,
            labels=["Positive Rotations","Negative Rotations"],
            autopct="%.2f%%")   # ax2 = pie plot with positive rotations and negative rotations
            # Alternatively: autopct=lambda pct : '{:.2f}%  ({:,.0f})'.format(pct,pct * sum(pie_vals)/100 
    ax2.set_title("Rotations")

    fig.tight_layout()
    plt.show()

def main():
    planet_data = []
    with open("planets.csv", newline="") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            name = row["Name"]
            mass = float(row["Mass"])
            diam = int(row["Diam"])
            dens = int(row["Density"])
            grav = float(row["Grav"])
            esc = float(row["Escape"])
            rot = float(row["Rotation"])
            day = float(row["Day"])
            dist = float(row["Distance"])
            per = float(row["Period"])
            moon = int(row["Moon"])
            temp = int(row["Temp"])
            
            planet_data.append({"Name": name,
                                "Mass": mass,
                                "Diam": diam,
                                "Dens": dens,
                                "Grav": grav,
                                "Esc": esc,
                                "Rot": rot,
                                "Day": day,
                                "Dist": dist,
                                "Per": per,
                                "Moon": moon,
                                "Temp": temp})

    # Open planet density bar graph (close window to continue program)
    plots(planet_data)
    
if __name__ == "__main__":
    main()