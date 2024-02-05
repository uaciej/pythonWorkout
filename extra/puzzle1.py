
CODES = [format(i, '04b') for i in range(16)]

def test_game():
    for code in CODES:
        for i in range(4):
            code = list(code)
            out = code[:]
            print(code)
            print(f'key is in {i+1}')
            roll = int(input('Which box to turn?: ')) - 1
            if roll == -1:
                print(f'no box turned {code}\n')
            else:
                if code[roll] == '0':
                    out[roll] = '1'
                else:
                    out[roll] = '0'
                print(f'box was turned {out}\n')


if __name__ == '__main__':
    test_game()