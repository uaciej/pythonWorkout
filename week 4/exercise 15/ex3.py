'''
 Open a log file from a Unix/Linux system—for example, one from the Apache
server. For each response code (i.e., three-digit code indicating the HTTP
request’s success or failure), store a list of IP addresses that generated that code
'''

def check_IP():
    with open ('logs.txt', 'r') as f:
        ip_dict = {}
        for line in f:
            words = line.split()
            ip_dict.setdefault(words[8], []).append(words[0])

    return ip_dict



if __name__ == "__main__":
    print(check_IP())