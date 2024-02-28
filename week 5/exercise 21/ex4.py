'''
Open an HTTP server’s log file. (If you lack one, then you can read one from
me at http://mng.bz/vxxM.) Summarize how many requests resulted in numeric
response codes—202, 304, and so on
'''

def open_log(file):
    output = {}
    with open(file, 'r') as f:
        for line in f:
            words = line.split()
            output[words[8]] = output.get(words[8], 0) + 1

    for key, val in output.items():
        print(f"{key}: {val}")


if __name__ == "__main__":
    open_log('../HTTPlogs.txt')