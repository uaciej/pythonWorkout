import random

def guessing_game():
    num = random.randint(0, 100)
    while True:
        digits = input("Guess the number: ")
        base = int(input("Base?: "))
        if base > 16:
            print("Base must be between 2 and 16")
            continue
        userNum = int(digits, base)
        if userNum == num:
            print("Just right!")
            break
        elif userNum > num:
            print("Too high!")
        else:
            print("Too low!")

if __name__ == "__main__":
    guessing_game()
