# type: ignore
""" Module with find_repeated_values function """
import random

# Generating a list of 100 random numbers in range from 1 to 10
values = [random.randint(1, 10) for _ in range(100)]


def find_repeated_values(val, n_times):
    """Find repeated values in a list."""

    # Creating an empty dictionary for counting numbers
    value_counts = {}

    # Creating a list of values that repeat at least n times
    res = []

    # Loop through each value in the list
    for value in val:
        # If the value already exists in the dictionary,
        # increase its counter
        # Current VALUE += 1
        # {value: i + 1}
        if value in value_counts:
            value_counts[value] += 1
            # # If the count = n_times, add to res
            if value_counts[value] == n_times:
                res.append(value)
        # If the value does not exist in the dictionary,
        # add it with a counter of 1
        # VALUE first time appears
        # {value: 1}
        else:
            value_counts[value] = 1

    return res


# Print the result
print(find_repeated_values(values, 10))
