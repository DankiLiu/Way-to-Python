import pygal
from die import Die


def roll_die():
    die = Die()

    # Make some rolls, and store results in a list.
    results = []
    for roll_num in range(100):
        result = die.roll()
        results.append(result)
    print(results)
    return die, results


def analyse_results(die, results: []):
    frequencies = []
    for value in range(1, die.num_sides + 1):
        frequency = results.count(value)
        frequencies.append(frequency)
    print("frequencies: ", frequencies)
    # Visualize the result.
    hist = pygal.Bar()
    hist.title = "Result of rolling one D6 1000 times."
    hist.x_labels = ['1', '2', '3', '4', '5', '6']
    hist.x_title = "Result"
    hist.y_title = "Frequency of Result"
    hist.add('D6', frequencies)
    hist.render_to_file('dis_visual.svg')


def rolling_two_dice():
    # Create two dice
    die_1 = Die()
    die_2 = Die()
    # Make some rolls and store results in a list.
    results = []
    for roll_num in range(100):
        result = die_1.roll() + die_2.roll()
        results.append(result)
    max_value = die_1.num_sides + die_2.num_sides
    frequencies = []
    for value in range(1, max_value + 1):
        frequency = results.count(value)
        frequencies.append(frequency)
    print("frequencies:{}".format(frequencies))

    hist = pygal.Bar()
    hist.title = "Results of rolling two D6 dice 1000 times."
    hist.x_labels = [str(i) for i in range(1, max_value + 1)]
    hist.x_title = "Result"
    hist.y_title = "Frequency of Result"
    hist.add("D6", frequencies)
    hist.render_to_file('dis_double_visual.svg')


if __name__ == '__main__':
    rolling_two_dice()