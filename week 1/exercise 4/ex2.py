def hex_output():
    x = input("Enter a hex number to convert: ")
    out = 0
    for i, elem in enumerate(reversed(x)):
        if elem.isdigit():
            out += (ord(elem.upper()) - 48) * 16**i
        elif (elem.upper() >= 'A' and elem.upper() <= 'F'):
            out += (ord(elem.upper()) - 55) * 16**i
        else:
            return ('Invalid character')
            
    return out

if __name__ == "__main__":
    print(hex_output())