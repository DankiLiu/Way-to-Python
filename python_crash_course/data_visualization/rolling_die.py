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
    print(frequencies)


if __name__ == '__main__':
    die, results = roll_die()
    analyse_results(die, results)