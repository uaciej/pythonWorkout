'''
Don’t write one function to find the largest word in a file that works on files and
another that works on the io.StringIO (http://mng.bz/PAOP) file simulator
used in testing. Write one function that works on both.
'''
import io

def largest_word(file):
    
    inside = file.read()
    words = inside.split()
    largest_word = max(words, key=len, default=None)

    return largest_word


if __name__ == "__main__":
    #Test file
    file_path = 'text.txt'
    with open(file_path, 'r') as file:
        result = largest_word(file)
    print(f"Largest word in {file_path}: {result}")

    #Test StringIO
    inside = "The authors of this paper are John Doe and Jane Smith. They argue that being short migh lead to self esteem issues and noticed a spike in depression in male subjects below 6 feet."
    string_io = io.StringIO(inside)
    result = largest_word(string_io)
    print(f"Largest word in io.StringIO: {result}")