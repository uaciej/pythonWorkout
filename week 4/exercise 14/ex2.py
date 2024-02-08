'''
 Create a dict in which the keys are usernames and the values are passwords,
both represented as strings. Create a tiny login system, in which the user must
enter a username and password. If there is a match, then indicate that the user
has successfully logged in. If not, then refuse them entry. (Note: This is a nice
little exercise, but please never store unencrypted passwords. It’s a major security risk.)
'''

DATABASE = {
    'user1': 'password1',
    'user2': 'password2',
    'user3': 'password3'
}

def login():
    user = input("Username: ")
    password = input("Password: ")
    if DATABASE.get(user) == password:
        print(f"Welcome {user}")
    else:
        print("Invalid credentials")


if __name__ == "__main__":
    login()