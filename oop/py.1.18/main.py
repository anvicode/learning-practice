# type: ignore
""" Module with create_dict_with_random_pairs function """
import random
import string

# Creating an empty dictionary
my_dict = {}


def create_dict_with_random_pairs():
    """Generates a dictionary with 100 random key-value pairs."""
    # Til the number of pairs is less than 100
    while len(my_dict) < 100:
        # Adding 100 random pairs to the dictionary
        for _ in range(100):
            # Making a random key from 1 to 100
            k = random.randint(1, 100)

            # Making a list from 5 random latin letters lower and upper case
            # and converting it to a string
            val = "".join(
                random.choices(string.ascii_lowercase + string.ascii_uppercase, k=5)
            )

            # Adding random key and generated value into the dictionary
            my_dict[k] = val

    return my_dict


if __name__ == "__main__":
    # Run the program
    create_dict_with_random_pairs()

    # Reading and printing all values by keys
    for key, value in my_dict.items():
        print(f"Key: {key}, Value: {value}")

    # Delete all pairs from the dictionary
    my_dict.clear()

    # Printing the empty dictionary
    print(f"Empty dictionary: {my_dict}")
