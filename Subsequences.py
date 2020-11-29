'''
Вася любит играть в игру Подпоследовательность.
Даны 2 строки, и нужно понять, является ли первая из них
подпоследовательностью второй. Когда строки достаточно длинные,
иногда очень трудно получить ответ на этот вопрос, просто посмотрев на них.
Помогите Васе, напишите функцию, которая решает эту задачу.
'''


def is_sub_string(subsequence, sequence):
    x = 0
    y = 0
    if subsequence == "":
        return True
    while y != len(sequence):
        if subsequence[x] == sequence[y]:
            if x == len(subsequence) - 1:
                return True
            x += 1
        y += 1
    return False


if __name__ == '__main__':
    subsequence = input()
    sequence = input()
    print(is_sub_string(subsequence, sequence))

# Time: 106ms, Memory: 4.20Mb
