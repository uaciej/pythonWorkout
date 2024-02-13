'''
 Read through a server (e.g., Apache or nginx) log file. What were the different
IP addresses that tried to access your server?
'''

def check_unique_IP(file):
    output = set()
    with open(file, 'r') as f:
        for line in f:
            words = line.split()
            output.add(words[0])
    
    return sorted(output)


if __name__ == "__main__":
    print(check_unique_IP('logs.txt'))