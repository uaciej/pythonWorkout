'''
Write an anyjoin function that works similarly to str.join, except that the first
argument is a sequence of any types (not just of strings), and the second argument is the “glue” that we put between elements, defaulting to " " (a space). So
anyjoin([1,2,3]) will return 1 2 3, and anyjoin('abc', pass:'**') will
return pass:a**b**c
'''

def anyjoin(sequence, glue=' '):
    return glue.join(map(str, sequence))


if __name__ == "__main__":
    print(anyjoin(range(1,4), '**'))