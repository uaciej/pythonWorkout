'''
For this exercise, I want you to write a function (calc) that expects a single
argument—a string containing a simple math expression in prefix notation—with an
operator and two numbers. Your program will parse the input and produce the appropriate output. 
For our purposes, it’s enough to handle the six basic arithmetic operations in Python: addition, subtraction, multiplication, division (/), modulus (%), and
exponentiation (**). The normal Python math rules should work, such that division
always results in a floating-point number. We’ll assume, for our purposes, that the
argument will only contain one of our six operators and two valid numbers
'''

def calc(expression):
    num1 = int(expression.split()[1])
    num2 = int(expression.split()[2])
    match expression.split()[0]:
        case '+':
            return num1 + num2
        case '-':
            return num1 - num2
        case '*':
            return num1 * num2
        case '/':
            return num1 / num2
        case '%':
            return num1 % num2
        case '**':
            return num1 ** num2



if  __name__ == "__main__":
    print('+ 2 3 ==>', calc('+ 2 3'))
    print('- 2 3 ==>', calc('- 2 3'))
    print('* 2 3 ==>', calc('* 2 3'))
    print('/ 2 3 ==>', calc('/ 2 3'))
    print('% 2 3 ==>', calc('% 2 3'))
    print('** 2 3 ==>', calc('** 2 3'))