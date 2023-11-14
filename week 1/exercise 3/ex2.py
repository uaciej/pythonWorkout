def idkFloat(x, y, z):
    before, after = str(x).split('.')
    newBefore = ''
    newAfter = ''
    for i, dig in enumerate(before):
        if i < len(before) - y:
            continue
        else:
            newBefore += dig
    for i, dig in enumerate(after):
        if i < z:
            newAfter += dig
    new = newBefore + '.' + newAfter
    return float(new)


if __name__ == "__main__":
    print(idkFloat(12345.67890, 2, 3))