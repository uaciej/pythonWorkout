'''
From /etc/passwd, create a dict in which the keys are the usernames (as in the
main exercise) and the values are themselves dicts with keys (and appropriate
values) for user ID, home directory, and shell.
'''


def passwd_to_dicts(file):
    
    with open(file, 'r') as f:
        output = {}
        for line in f:
           if not line.startswith(('#', '\n')):
               userdata = line.split(':')
               username = userdata[0].strip()
               output[username] = {
                   'user_id' : userdata[2].strip(),
                   'home_directory' : userdata[-2].strip(),
                   'user_shell' : userdata[-1].strip()
                   }

        return output
    

if __name__ == "__main__":
    print(passwd_to_dicts('../passwords.txt'))