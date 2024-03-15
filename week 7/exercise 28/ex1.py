'''
For this exercise, write a function (join_numbers) that takes a range of integers.
The function should return those numbers as a string, with commas between the
numbers. 
'''

def join_numbers(int_range):
    return ','.join(map(str, int_range))
    # return ','.join([str(num) for num in int_range])


if  __name__ == '__main__':
    print(join_numbers(range(15)))