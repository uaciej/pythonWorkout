import random

def guessing_game():
    tries = 3
    num = random.randint(0, 100)
    while True:
        if tries == 0:
            print("You lose!")
            break
        tries -= 1
        userNum = int(input(f"You have {tries+1} tries. Guess the number: "))
        if userNum == num:
            print("Just right!")
            break
        elif userNum > num:
            print("Too high!")
        else:
            print("Too low!")

if __name__ == "__main__":
    guessing_game()
