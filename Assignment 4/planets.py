import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from statistics import *

def main():
    data = pd.read_csv('planets.csv')

    diameter = data["Diam"]
    mass = data["Mass"]
    print('Correlation between diameter and mass:\n', np.corrcoef(diameter, mass))
    print('There is a strong correlation between diameter and mass.')
    print()

    distance = data["Distance"]
    temp = data["Temp"]
    print('Correlation between distance and temp:\n', np.corrcoef(distance, temp))
    print('There is a considerably anticorrelation between distance and temp.')
    print('The scatter plot reveals a logarithmic relationship.')
    print('Venus is the exception to this relationship.')
    print()
    plt.title('temp vs distance')
    plt.scatter(distance, temp)
    plt.show()
    
    period = data['Period']
    day = data['Day']
    print('Correlation between period and day:\n', np.corrcoef(period, day))
    print('There is a weak anticorrelation between period and day.')

if __name__ == "__main__":
    main()