# Darrik Houck

from statistics import *

def highest_rainfall(list):
    return max(list, key=lambda cities : cities[1])

def lowest_rainfall(list):
    return min(list, key=lambda cities : cities[1])

def mean_rainfall(list):
    return mean([cities[1] for cities in list])

def cities_grtr_mean(list):
    mean = mean_rainfall(list)
    num = 0
    city_list = []
    for cities in list:
        if cities[1] > mean:
            num += 1
            city_list.append(cities[0])
    return num, city_list

def main():

    # Open rainfall.txt and create list of tuples
    file = open("rainfall.txt", "r")
    data = []
    data.extend(line.split() for line in file)
    # Cast inches from string to float and convert to centimeters
    for cities in data:
        cities[1] = float(cities[1]) * 2.54
    
    # Convert list of lists to list of tuples
    data = [tuple(cities) for cities in data]

    # Max rainfall and min rainfall functions
    print("City with most rainfall: {}. {:.3f} cm".format(*highest_rainfall(data)))
    print("City with least rainfall: {}. {:.3f} cm".format(*lowest_rainfall(data)))

    # Mean rainfall function
    print("Mean rainfall: {:.3f} cm".format(mean_rainfall(data)))

    # Number of cities with rainfall greater than mean
    cities_mean = cities_grtr_mean(data)
    print(("Cities with more rainfall than the mean: {}." + " {}" * len(cities_mean[1])).format(cities_mean[0], *cities_mean[1]))

if __name__ == "__main__":
    main()

# Test Output:
# City with most rainfall: Daly. 97.079 cm
# City with least rainfall: Akron. 65.557 cm
# Mean rainfall: 86.511 cm
# Cities with more rainfall than the mean: 14. Albia AmesW Anamosa Atlantic Beaconsfield Bedford BellePlaine Bellevue Blcokton Bloomfield Boone BurlingtonKBUR Burlington Daly