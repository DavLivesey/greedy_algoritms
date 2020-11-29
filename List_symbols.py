
def is_correct_bracket_seq(sequence):
    element_dict = {
        'begin_symbols': ('[', '(', '{'),
        'finish_symbols': (']', ')', '}')
    }
    start = 0
    end = -1
    open_symbol = element_dict['begin_symbols'].index(sequence[start])
    close_symbol = element_dict['finish_symbols'].index(sequence[end])
    while -start != end:
        print(-start)
        print(end)
        if sequence[start] not in element_dict['begin_symbols']\
            or sequence[end] not in element_dict['finish_symbols']:
            return False
    return True




if __name__ == '__main__':
    sequence = input()
    print(is_correct_bracket_seq(sequence))
