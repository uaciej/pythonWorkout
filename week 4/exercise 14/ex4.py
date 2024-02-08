'''
 Define a dict whose keys are names of people in your family, and whose values
are their birth dates, as represented by Python date objects (http://mng.bz/
jggr). Ask the user to enter the name of someone in your family, and have the
program calculate how many days old that person is. 
'''
from datetime import datetime

BIRTHDAYS = {
    'Szymon' : datetime(2022, 2, 4),
    'Sylwia' : datetime(1994, 9, 11),
    'Maciej' : datetime(1994, 10, 17)
}

def calculate_days_old(birthdate):
    today = datetime.now()
    days_old = (today - birthdate).days
    return days_old




if __name__ == "__main__":
    name = (input("Enter the name of someone you know. "))   
    if name not in BIRTHDAYS:
        print("Incorrect person")
    else:
        age = calculate_days_old(BIRTHDAYS[name])
        print("%s is %d days old" % (name, age))