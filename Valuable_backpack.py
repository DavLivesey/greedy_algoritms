'''Реализуйте код алгоритма заполнения рюкзака, рассмотренного в лекции:
Взять наиболее ценный предмет, который поместится в рюкзак.
Выбрать следующий по стоимости товар с учётом того, что для него осталось
место в рюкзаке.'''


def valuable_backpack(backpack_capacity, object_list):
    object_list = sorted(enumerate(object_list),
                         key=lambda x: (-int(x[1][0]), int(x[1][1])))
    x = 0
    result = []
    while x != len(object_list):
        if int(object_list[x][1][1]) <= backpack_capacity:
            result.append(object_list[x][0])
            backpack_capacity -= int(object_list[x][1][1])
        x += 1
    return ' '.join(repr(e) for e in sorted(result))


if __name__ == '__main__':
    backpack_capacity = int(input())
    count_objects = int(input())
    object_list = []
    for num in range(count_objects):
        object = list(input().split(' '))
        object_list.append(object)
    print(valuable_backpack(backpack_capacity, object_list))

# Time: 92ms, Memory: 6.47Mb
