'''
 Reading from that same server log, what response codes were returned to
users? The 200 code represents “OK,” but there are also 403, 404, and 500
errors.
'''

def check_unique_response_codes(file):
    output = set()
    with open(file, 'r') as f:
        for line in f:
            words = line.split()
            output.add(words[8])
    
    return sorted(output)


if __name__ == "__main__":
    print(check_unique_response_codes('logs.txt'))