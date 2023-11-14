def myavg(nums):
    out = 0
    for num in nums:
        out += num
    return out / len(nums)

print(myavg((1,2,3,4))) # 2.5