'''
 In the /etc/passwd file you used earlier, what different shells (i.e., command
interpreters, named in the final field on each line) are assigned to users? Use a
set comprehension to gather them.
'''

def diff_shells(file):
    with open(file) as f:
        return {line.split(':')[-1] for line in f if not line.startswith(('#', '\n'))}



if __name__ == "__main__":
    print(diff_shells('../assets/passwords.txt'))