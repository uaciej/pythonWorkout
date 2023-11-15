def hex_output():
    x = input("Enter a hex number to convert: ")
    out = 0
    for i, elem in enumerate(reversed(x)):
        out += int(elem, 16) * 16**i
    return out

if __name__ == "__main__":
    print(hex_output())