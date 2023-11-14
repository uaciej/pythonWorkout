def mysum(*nums):
    out = 0
    for num in nums:
        out += num
    return out

print(mysum(1,2,3,4)) # 10