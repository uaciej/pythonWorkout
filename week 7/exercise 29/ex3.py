'''
 In the United States, phone numbers have 10 digits—a three-digit area code,
followed by a seven-digit number. Several times during my childhood, area
codes would run out of phone numbers, forcing half of the population to get a
new area code. After such a split, XXX-YYY-ZZZZ might remain XXX-YYY-ZZZZ,
or it might become NNN-YYY-ZZZZ, with NNN being the new area code. The
decision regarding which numbers remained and which changed was often
made based on the phone numbers’ final seven digits. Use a list comprehension
to return a new list of strings, in which any phone number whose YYY begins
with the digits 0–5 will have its area code changed to XXX+1. For example,
given the list of strings ['123-456-7890', '123-333-4444', '123-777-8888'],
we want to convert them to ['124-456-7890', '124-333-4444', '124-777-
8888'].
'''


def change_phone(lst):
    return [
        '-'.join([str(int(phone.split('-')[0]) +1), phone.split('-')[1], phone.split('-')[2]])
        if int(phone.split('-')[1][0]) < 6
        else phone for phone in lst
        ]


if __name__ == "__main__":
    print(change_phone(['123-456-7890', '123-333-4444', '123-777-8888']))