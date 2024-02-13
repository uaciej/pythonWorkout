'''
 Write a function, called how_many_different_numbers, that
takes a single list of integers and returns the number of different integers it contains.
'''

def how_many_different_numbers(lis):
    return len(set(lis))


if __name__ == "__main__":
    print(how_many_different_numbers((1, 2, 3, 4, 5, 1, 3, 5, 7)))