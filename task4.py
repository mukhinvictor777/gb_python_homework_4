"""
Представлен список чисел. Определить элементы списка, не имеющие повторений.
Сформировать итоговый массив чисел, соответствующих требованию.
Элементы вывести в порядке их следования в исходном списке. Для выполнения задания обязательно использовать генератор.
Пример исходного списка: [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11].
Результат: [23, 1, 3, 10, 4, 11]
"""
task_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
result_list = []
for i in range(0, len(task_list)):
    duplication = 0
    j = 0
    k = i + 1
    while duplication == 0 and j < i:
        if task_list[i] == task_list[j]:
            duplication = 1
        else:
            j += 1
    while duplication == 0 and k < len(task_list):
        if task_list[i] == task_list[k]:
            duplication = 1
        else:
            k += 1
    if duplication == 0:
        result_list.append(task_list[i])
print(result_list)


