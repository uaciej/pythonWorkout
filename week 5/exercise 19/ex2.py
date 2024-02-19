'''
Read through /etc/passwd, creating a dict in which user login shells (the final
field on each line) are the keys. Each value will be a list of the users for whom
that shell is defined as their login shell.
'''


def passwd_to_dict(file):
    
    with open(file, 'r') as f:
        output = {}
        for line in f:
           if not line.startswith(('#', '\n')):
               userdata = line.split(':')
               user_shell = userdata[-1].strip()
               output[user_shell] = output.get(user_shell, []) + [userdata[0]]
        return output
    

if __name__ == "__main__":
    print(passwd_to_dict('../passwords.txt'))