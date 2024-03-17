'''
take a sequence of strings, turn them into
numbers, and then sum them. But we’re going to make it a bit more complicated,
because we’re going to filter out those strings that can’t be turned into integers.
'''

def sum_numbers(s):
    return sum([int(num) for num in s.split() if num.isdigit()])


if __name__ == '__main__':
    print(sum_numbers('10 abc 20 de44 30 55fg 40'))