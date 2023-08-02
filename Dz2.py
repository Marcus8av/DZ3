# Дан список повторяющихся элементов. 
# Вернуть список с дублирующимися элементами. 
# В результирующем списке не должно быть дубликатов.

large_list = [6, 2, 4, 9, 2, 7, 18, 12, 7, 11, 12, 28, 17, 3, 25]

my_set = set()

for item in large_list:
    if large_list.count(item) > 1:
        my_set.add(item)
print("Сам список", large_list)
print("Дубликаты в списке", list(my_set))
