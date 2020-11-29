'''
Евлампия выбрала себе классный дом.
Правда в нём нет лифтов, хотя этажей много.
Она решила, что ходить по лестницам долго и можно прыгать по ступенькам.
Дом старинный, ступеньки в нём разного размера.
Для каждой ступеньки известно, на какое максимальное
количество ступенек вверх с неё можно допрыгнуть.
Нужно помочь Евлампии определить, сможет ли она добраться
с нижней ступеньки на верхнюю.
'''


def ladder(count_stairs, stair):
    x = 0
    while x < count_stairs:
        if stair[x] == 0:
            return False
        if stair[x] >= count_stairs - x:
            break
        y = x + 1
        x += stair[x]
        max_y = 0
        index_y = 0
        while y <= x:
            if stair[y] > max_y:
                max_y = stair[y]
                index_y = y
            y += 1
        x = index_y
        if max_y == 0:
            return False
    return True


if __name__ == '__main__':
    count_stairs = int(input())
    stair = list(map(int, input().split(' ')))
    print(ladder(count_stairs, stair))

# Time: 47ms, Memory: 4.17Mb
