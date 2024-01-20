'''
Given a list of lists, with each list containing zero or more numbers, sort by the
sum of each inner list’s numbers.
'''

def sum_of_nums_in_list(lis):
    return sorted(lis, key=sum, reverse=True)


if __name__ == "__main__":
    lis = []
    for i in range(10):
        lis.append(list(range(i)))
    print(lis)
    print (sum_of_nums_in_list(lis))