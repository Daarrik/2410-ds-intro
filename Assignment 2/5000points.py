import matplotlib.pyplot as plt

def main():
    data = open("5000_points.txt", "r")
    
    x = []
    y = []
    for row in data:
        x.append(int(row.split()[0]))
        y.append(int(row.split()[1]))

    # This comment block has another way to make x and y lists with some Python list comprehension
    # Did not use because makes 3 lists as opposed to two. List points is essentially a duplicate of lists x and y
    # Still cool to look at though
    # points = []
    # points.extend(tuple([int(num) for num in row.split()]) for row in data)
    # # Does the same as:
    # # for row in data:
    # #     coord = [int(num) for num in row.split()]
    # #     points.append(tuple(coord))
    # x = [point[0] for point in points]
    # y = [point[1] for point in points]

    # Part 1
    # One color for all points
    plt.figure("Scatter: One color")
    plt.scatter(x, y)
    plt.title("Points")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.show()

    # Part 2
    # List comprehension to separate even and odd points
    even_x = [x[index] for index in range(0, len(x), 2)]    
    even_y = [y[index] for index in range(0, len(x), 2)]
    odd_x = [x[index] for index in range(1, len(y), 2)]
    odd_y = [y[index] for index in range(1, len(y), 2)]

    # Even points red, odd points green
    plt.figure("Scatter: Two colors")
    plt.scatter(even_x, even_y, color="red")
    plt.scatter(odd_x, odd_y, color="green")
    plt.title("Points: Two Colors")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.show()

    # Part 3
    x_grtr_y = len([value for i, value in enumerate(x) if x[i] > y[i]])
    x_less_y = len([value for i, value in enumerate(x) if x[i] < y[i]])
    x_eql_y = len([value for i, value in enumerate(x) if x[i] == y[i]])
    bar_labels = ["X less than Y", "X equal to Y", "X greater than Y"]

    # Bar plot of (x > y, x < y, x == y)
    plt.figure("X and Y")
    plt.bar(x=bar_labels,
            height=[x_less_y, x_eql_y, x_grtr_y])
    plt.ylabel("Amount in data")
    plt.show()
    
    # Part 4
    # Horizontal version of the bar plot above
    plt.figure("Horizontal X and Y")
    plt.barh(y=bar_labels,
            width=[x_less_y, x_eql_y, x_grtr_y])
    plt.title("Horizontal X and Y")
    plt.xlabel("Amount in data")
    plt.yticks(rotation = 45)
    plt.show()

if __name__ == "__main__":
    main()