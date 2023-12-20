'''
 Don’t write one function that squares integers, and another that squares floats.
Write one function that handles all numbers.
'''


def square_all(num):
    return num ** 2


def convert_input(string):
    try:
        # Try converting to an integer first
        return int(string)
    except ValueError:
        try:
            # If it fails, try converting to a float
            return float(string)
        except ValueError:
            # If both conversions fail, the input is not a valid number
            print("Invalid input. Please enter a valid number.")
            exit()


if __name__ == "__main__":
    num = convert_input(input("What number should we square? "))
    print(square_all(num))