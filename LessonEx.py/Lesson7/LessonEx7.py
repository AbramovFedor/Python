# Планеты вращаются вокруг звезд по эллиптическим орбитам.
# Назовем самой далекой планетой ту, орбита которой имеет
# самую большую площадь. Напишите функцию
# find_farthest_orbit(list_of_orbits),
# которая среди списка орбит планет найдет ту,
# по которой вращается самая далекая планета

# def find_farthest_orbit(array):
#     max_sq = [(i[0] * i[1], i) for i in array if i[0] != i[1]]
#     return max(max_sq)[1]

# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
# print(*find_farthest_orbit(orbits))

#--------------------------------------------------------------------

# Напишите функцию same_by(characteristic, objects),
# которая проверяет, все ли объекты имеют одинаковое
# значение некоторой характеристики, и возвращают True,
# если это так. Если значение характеристики для
# разных объектов отличается - то False.
# Для пустого набора объектов,
# функция должна возвращать True.
# Аргумент characteristic - это функция,
# которая принимает объект и вычисляет его характеристику.

def same_by(condition, nums):
    return len(set(map(condition, nums))) == 1


values = [2, 3, 6, 4]

if same_by(lambda x: x % 2, values):
    print('same')
else:
    print('different')