def name_triangle():
    name = input("What is your name?: ")
    for i, _ in enumerate(name):
        print (name[:i+1])


if __name__ == "__main__":
    name_triangle()