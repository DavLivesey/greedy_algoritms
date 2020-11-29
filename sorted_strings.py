'''
После чая с печеньками ребята решили поиграть в игру.
Дан набор строк одинаковой длины, состоящих из маленьких латинских букв.
Нужно определить, какое минимальное число позиций в каждой из
строк нужно удалить, чтобы буквы в строках, соответствующие каждому
индексу из оставшихся,были лексикографически отсортированы по неубыванию
(то есть последовательности, читающиеся сверху вниз,
должны быть отсортированы по неубыванию).
Как происходит удаление – один столбец полностью берет и уничтожается.
'''


def sorted_strings(count_strings, length_strings, strings):
    x = 0
    y = 0
    count_del = 0
    while x < length_strings and count_strings > 1:
        if strings[y][x] > strings[y+1][x]:
            count_del += 1
            print(y, strings[y][x], x)
            x += 1
            y = 0
        else:
            print(strings[y][x], strings[y+1][x])
            y += 1
        if y >= count_strings - 1:
            y = 0
            x += 1
    return count_del


if __name__ == '__main__':
    count_strings = int(input())
    length_strings = int(input())
    strings = []
    for i in range(count_strings):
        strings.append(input())
    print(sorted_strings(count_strings, length_strings, strings))

# Time: 50ms, Memory: 3.97Mb
