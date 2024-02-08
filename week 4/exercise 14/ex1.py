'''
In this exercise, I want you to create a new constant dict, called MENU, representing
the possible items you can order at a restaurant. The keys will be strings, and the values will be prices (i.e., integers). You should then write a function, restaurant, that
asks the user to enter an order:
 If the user enters the name of a dish on the menu, the program prints the price
and the running total. It then asks the user again for their order.
 If the user enters the name of a dish not on the menu, the program scolds the
user (mildly). It then asks the user again for their order.
 If the user enters an empty string, the program stops prompting and prints the
total amount.
For example, a session with the user might look like this:
Order: sandwich
sandwich costs 10, total is 10
Order: tea
tea costs 7, total is 17
Order: elephant
Sorry, we are fresh out of elephant today.
Order: <enter>
Your total is 17
Note that you can always check to see if a key is in a dict with the in operator. That
returns True or False
'''

MENU = {'sandwich': 10, 'tea': 7, 'salad': 9}

def restaurant():
    
    total = 0
    while True:
        order = input("Enter your order: ").strip().lower()
        
        if not order:
            break

        if order in MENU:
            total += MENU[order]
            print(f"{order} costs {MENU[order]}, total is {total}")
        else:
            print(f"Sorry, we are fresh out of {order}.")
            
    print(f"Your total is {total}.")

if __name__ == "__main__":
    restaurant()