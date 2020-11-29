'''
Помогите Алле написать код алгоритма для выбора уроков,
которые пройдут в классе. Дано расписание предметов.
Нужно составить расписание, в соответствии с которым в классе можно
будет провести как можно больше уроков.
'''

count_lessons = int(input())
lessons_list = []
for num in range(count_lessons):
    lesson = list(input().split(' '))
    lessons_list.append(lesson)
lessons_list.sort(key=lambda time_finish: (float(time_finish[1]), float(time_finish[0])))
x = 0
y = 1
while x != len(lessons_list) - 1:
    if float(lessons_list[y][0]) < float(lessons_list[x][1]):
        del lessons_list[y]
    else:
        x += 1
        y += 1
print(len(lessons_list))
for i in lessons_list:
    print(' '.join(i))

# Time: 46ms, Memory: 4.12Mb