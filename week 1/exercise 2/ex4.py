def myfunc(words):
    out = 0
    short = 100
    long = 0
    for word in words:
        x = len(word)
        out += x
        if x < short:
            short = x
        if x > long:
            long = x

    tup = (short, long, out/len(words))
    return tup

print(myfunc(("bro", "likes", "to", "code", "cringe"))) # (2, 6, 4.0)