'''
Create a text file (using an editor, not necessarily Python) containing two tab separated columns, with each column containing a number. Then use Python
to read through the file you’ve created. For each line, multiply each first number by the second, and then sum the results 
'''
def multiply_and_sum_columns(file):
     
    with open(file, 'r') as f:
        out = 0
        for line in f:
            nums = line.split()
            line_score = int(nums[0]) * int(nums[1])
            out += line_score

    return out

if __name__ == "__main__":
    print(multiply_and_sum_columns('../nums.txt'))