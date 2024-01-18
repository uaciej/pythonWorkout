'''
Given a sequence of positive and negative numbers, sort them by absolute valu
'''

def sort_absolute(*nums):
    return sorted(nums, key=abs)


if __name__ == "__main__":
    nums = [12, -45, 78, -39, 46, -2, 120, -200]
    print("Original List: ", nums)
    print("Sorted List: ", sort_absolute(*nums))