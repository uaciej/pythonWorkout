'''
 The final field in /etc/passwd is the shell, the Unix command interpreter that’s
invoked when a user logs in. Create a file, containing one line per shell, in
which the shell’s name is written, followed by all of the usernames that use the
shell; for example
'''

def create_shell_users_file(input_file, output_file):
    with open(input_file,'r') as inf,  open(output_file, 'w') as outf:
        dic = {}
        for line in inf:
            if not line.startswith(('#', '\n')):
                words = line.split(':')
                shell = words[-1].strip()
                dic[shell] = dic.get(shell, []) + [words[0]]
        for key, val in dic.items():
            outf.write(f"{key}, {', '.join(val)} \n")




if __name__ == "__main__":
    create_shell_users_file('../passwords.txt', '../passwords_shell_users.txt')