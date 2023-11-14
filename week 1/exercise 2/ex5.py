def myfunc(objects):
    out = 0
    for obj in objects:
        try:
            out += int(obj)
        except:
            pass
    return out

print(myfunc((1, 2, 3, "cat", "4", (1, 2, 3) ))) # 10 -> 1+2+3+4