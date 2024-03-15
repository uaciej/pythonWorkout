'''
 Given a list of strings containing hexadecimal numbers, sum the numbers
together.
'''

def hex_sum(lst):
    return sum([int(num, 16) for num in lst])



if __name__ == "__main__":
    hex_strings = [
    "0x123",
    "0xABC",
    "0xFF0",
    "0x1A2",
    "0xDEA",
    "0x8BA",
    "0xC0",
    "0xDEC",
    "0xBAA",
    "0xCAF"
]
    print(hex_sum(hex_strings))