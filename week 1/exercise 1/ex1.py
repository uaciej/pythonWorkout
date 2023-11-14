import random

def guessing_game():
    num = random.randint(0, 100)
    while True:
        userNum = int(input("Guess the number: "))
        if userNum == num:
            print("Just right!")
            break
        elif userNum > num:
            print("Too high!")
        else:
            print("Too low!")

if __name__ == "__main__":
    guessing_game()
