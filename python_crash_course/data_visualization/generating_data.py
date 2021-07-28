import matplotlib.pyplot as plt

from random_walk import RandomWalk


def plot_squares():
    input_values = [1, 2, 3, 4, 5]
    squares = [1, 4, 9, 16, 25]
    plt.plot(input_values, squares, linewidth=5)

    # Set chart title and label axes.
    plt.title("Square Numbers", fontsize=24)
    plt.xlabel("Value", fontsize=16)
    plt.ylabel("Square of Value", fontsize=16)

    # Set size of tick labels.
    plt.tick_params(axis='both', labelsize=14)
    plt.show()


def plot_squares_cmap():
    x_values = list(range(1, 1001))
    y_values = [x**2 for x in x_values]

    plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, edgecolors='none', s=20)

    # Set chart title and label axes.
    plt.title("Square Numbers", fontsize=24)
    plt.xlabel("Value", fontsize=16)
    plt.ylabel("Square of Value", fontsize=16)

    # Set size of tick labels.
    plt.tick_params(axis='both', labelsize=14)

    # Set the range for each axis.
    plt.axis([0, 1100, 0, 1100000])

    plt.show()


def plot_random_walk():
    while True:
        rw = RandomWalk()
        rw.fill_walk()

        point_numbers = list(range(rw.num_points))
        plt.scatter(rw.x_value, rw.y_value, c=point_numbers, cmap=plt.cm.Blues,
                    edgecolors='none', s=3)

        # Emphasize the first and last points.
        # plt.scatter(0, 0, c='green', edgecolors='none', s=50)
        # plt.scatter(rw.x_value[-1], rw.y_value[-1], c='red', edgecolors='none', s=50)

        # Remove the axes.
        plt.axis('off')
        plt.figure(figsize=(10, 6))
        plt.show()

        keep_running = input("Make another walk? (y/n): ")
        if keep_running == 'n':
            break
