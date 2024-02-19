'''
Ask the user to enter integers, separated by spaces. From this input, create a
dict whose keys are the factors for each number, and the values are lists containing those of the users’ integers that are multiples of those factors.
'''


def ints_with_factors():
    output = {}
    nums = input("Provide space-separated integers: ").split()
    for num in nums:
        num = int(num)
        for i in range(1, num//2 + 1):
            if num % i == 0:
                output[i] = output.get(i, [])
                output[i].append(num)
    return output


if __name__ == "__main__":
    print(ints_with_factors())