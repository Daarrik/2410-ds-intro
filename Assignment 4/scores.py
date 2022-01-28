import pandas as pd
import matplotlib.pyplot as plt
from statistics import *

def main():
    data = pd.read_csv('scores.csv')
    test_means = []

    for column in data:
        print(f'{column} data:')
        print(f'max: {max(data[column]):.2f}')
        print(f'max: {min(data[column]):.2f}')
        print(f'max: {max(data[column]) - min(data[column]):.2f}')
        column_mean = mean(data[column])
        print(f'mean: {column_mean:.2f}')
        # Ugly check, could probably be better
        if column == "Test 1" or column == "Test 2" or column == "Test 3":
            test_means.append((column, column_mean))
        print(f'variance: {variance(data[column]):.2f}')
        print(f'standard deviation: {stdev(data[column]):.2f}')
        print()

    best_test = max(test_means, key = lambda test : test[1])[0]
    print(f'Students did best on {best_test} because the mean for this test was the highest of all the tests.')
    
    test_data = ["Test 1", "Test 2", "Test 3"]

    print('Boxplot for Test 1:')
    print('The top and bottom edges of the box are the upper quartile and lower quartile of this test.')
    print('The green line is the median of the test.')
    print('The horizontal lines at the top and bottom of the boxplot are the highest and lowest test scores that are not outliers.')
    print('The test had 3 outliers which did not fit into the lower nor upper quartiles.')
    data.boxplot(column=["Test 1", "Test 2", "Test 3"])
    plt.show()
    
if __name__ == "__main__":
    main()