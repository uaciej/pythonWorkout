'''
In this exercise, write a function (get_final_line) that takes a filename as an
argument. The function should return that file’s final line on the screen
'''

def get_final_line(file):
    
    with open(file, 'r') as f:
        output = ''
        for line in f:
           output = line
    
    return output

if __name__ == "__main__":
    print(get_final_line('../text.txt'))