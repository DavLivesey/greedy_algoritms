n = int(input())
m = int(input())
string = [input().split() for i in range(n)]
long = 0
height = 0
delited = 0
while long < n:
    print(string[long][height])
    print(string[long][height], string[long][height+1])
    if string[long][height] < string[long][height+1]:
        height += 1
    else:
        delited += 1
        height = 0
        long += 1
    if height + 1 < m:
        height = 0
        long += 1
