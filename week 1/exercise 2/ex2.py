def mysum(nums, start=0):
    out = 0
    for num in nums:
        out += num
    return out + start

print(mysum((1,2,3),4)) # 10