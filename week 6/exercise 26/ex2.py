'''
 Expand the program you wrote, such that the user’s input can contain any
number of numbers, not just two. The program will thus handle + 3 5 7 or / 100
5 5, and will apply the operator from left to right—giving the answers 15 and 4,
respectively.
'''
import operator

def calc(expression):
    operant, *nums = expression.split()
    nums = list(map(int, nums))
    operations = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv,
        '%': operator.mod,
        '**': operator.pow,
    }

    op = operations[operant]

    while len(nums)>1:
        a,b=nums.pop(0),nums.pop(0)
        nums.insert(0, op(a, b))
    return nums[0]



if  __name__ == "__main__":
    print('+ 2 3 4 ==>', calc('+ 2 3 4'))
    print('- 2 3 4 ==>', calc('- 2 3 4'))
    print('* 2 3 4 ==>', calc('* 2 3 4'))
    print('/ 2 3 4 5 ==>', calc('/ 2 3 4 5'))
    print('% 2 3 4 5 ==>', calc('% 2 3 4 5'))
    print('** 2 3 4 6 ==>', calc('** 2 3 4 6'))