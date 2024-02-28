'''
Use the hashlib module in the Python standard library, and the md5 function
within it, to calculate the MD5 hash for the contents of every file in a userspecified directory. Then print all of the filenames and their MD5 hashes.
'''
import os
import hashlib

def calculate_md5(file):
    md5 = hashlib.md5()
    with open(file, 'rb') as f:
        for chunk in iter(lambda: f.read(4096), b''):
            md5.update(chunk)
    return md5.hexdigest()


def find_all_longest_words(directory):
    output = {}
    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)
        if os.path.isfile(filepath):
            output[filename] = calculate_md5(filepath)

    for key, val in output.items():
        print(f"{key}: {val}")


if __name__ == "__main__":
    find_all_longest_words('..')