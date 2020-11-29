'''
Во сне Гоша долго играл в игру Лампочка.
Он то выигрывал, то проигрывал.
Ему стало интересно, сколько максимум партий подряд он
получал большее количество очков, чем в предыдущей.
'''

count_strikes = int(input())
strikes = list(map(int, input().split(' ')))
max_combo = 0
max_list = []
for i in range(len(strikes)):
    if int(strikes[i]) > int(strikes[i-1]):
        max_combo += 1
    else:
        max_list.append(max_combo)
        max_combo = 1
max_list.append(max_combo)
max_list.sort()
print(max_list[-1])

# Time: 168ms, Memory: 11.97Mb
