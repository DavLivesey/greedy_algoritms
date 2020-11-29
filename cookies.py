'''
К Васе в гости пришли одноклассники. Его мама решила угостить ребят печеньем.
Но не всё так просто. Печенья могут быть разного размера.
У каждого ребёнка есть фактор жадности — минимальный размер печенья,
которое он возьмёт. Нужно выяснить, сколько ребят останутся довольными.
Каждый ребёнок может взять не больше одного печенья.
'''


def cookies_function(count_childrens, factor_greed, cookies):
    cookies.sort()
    factor_greed.sort()
    x = 0
    y = 0
    funny_children = 0
    while x < count_childrens and y < len(cookies):
        cooki = int(cookies[y])
        greedy = int(factor_greed[x])
        if cooki >= greedy:
            funny_children += 1
            cookies[y] = 0
            x += 1
        y += 1
    return funny_children


if __name__ == '__main__':
    count_childrens = int(input())
    factor_greed = list(map(int, input().split(' ')))
    count_cookies = int(input())
    cookies = list(map(int, input().split(' ')))
    print(cookies_function(count_childrens, factor_greed, cookies))

# Time: 58ms, Memory: 3.95Mb
