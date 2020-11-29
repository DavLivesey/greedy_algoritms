'''
Дочь Кондратия Евлампия решила купить в ипотеку несколько домов
на территории Трешландии. Она нашла n объявлений о продаже.
Известна стоимость каждого дома в трешландских франках.
Евлампия может позволить себе взять ипотеку на общую сумму k франков.
Нужно помочь ей определить,
какое наибольшее количество домов можно купить на эти деньги.
'''

count_houses_and_max_cost = list(map(int, input().split()))
list_houses = list(map(int, input().split()))
x = 0
list_houses.sort()
result = 0
while x != count_houses_and_max_cost[0]:
    if list_houses[x] <= count_houses_and_max_cost[1]:
        result += 1
        count_houses_and_max_cost[1] = (
                count_houses_and_max_cost[1] - list_houses[x]
        )
    x += 1
print(result)

# Time: 43ms, Memory: 4.21Mb