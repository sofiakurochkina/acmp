# корвет Эния (боевой надводный военный корабль)
# 1кв метр панели = 1 нанограмм сульфида 
# нужно обработать N панелей размером (А на В метров)
# Сколько сульфида необходимо на обработку всех панелей с двух сторон

# N ≤ 100 панелей
# A ≤ 100 длина
# B ≤ 100 ширина

inputs = input ()
split_nums = inputs.split(' ')

N = int(split_nums[0])
A = int(split_nums[1])
B = int(split_nums[2])

obrabotka = N*A*B*2
print(obrabotka)