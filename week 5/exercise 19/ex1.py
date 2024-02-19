'''
In this exercise, write a function, passwd_to_dict, that reads from a Unix-style
“password file,” commonly stored as /etc/passwd, and returns a dict based on it
'''

def passwd_to_dict(file):
    
    with open(file, 'r') as f:
        output = {}
        for line in f:
           if not line.startswith(('#', '\n')):
               userdata = line.split(':')
               username = userdata[0]
               user_id = userdata[2]
               output[username] = int(user_id)
               
    return output

if __name__ == "__main__":
    print(passwd_to_dict('../passwords.txt'))