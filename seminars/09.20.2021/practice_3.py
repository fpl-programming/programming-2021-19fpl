# pylint: skip-file
"""
Practice 3
Data Structures: Queue
"""

# Task 1
"""
Написать функцию извлечения элементов из очереди до тех пор,
пока первый элемент очереди не станет четным.
"""
array = [1, 3, 4, 5, 6, 7]
queue_ = array

while queue_[0] % 2:
    queue_.pop(0)

print(queue_)

# Task 2
"""
Дан набор из 10 целых чисел. 
Создать две очереди: первая должна содержать все нечетные, 
а вторая — все четные числа из исходного набора 
(порядок чисел в каждой очереди должен совпадать с порядком чисел в исходном наборе).
"""
array = [1, 3, 4, 5, 6, 7]
queue_1 = []
queue_2 = []

# front --- back
for element in array:
    if element % 2:
        queue_1.append(element)
    else:
        queue_2.append(element)

print(queue_1)
print(queue_2)

# Task 3
"""
https://informatics.msk.ru/mod/statements/view.php?id=20210&chapterid=50#1
"""
cards_1 = [1, 3, 5, 7, 9]
cards_2 = [2, 4, 6, 8, 0]
# cards_1 = [7, 3, 5, 9, 6]
# cards_2 = [2, 4, 6, 8, 0]

counter = 0

# front --- back
while cards_1 and cards_2:
    counter += 1
    element_1 = cards_1.pop(0)
    element_2 = cards_2.pop(0)

    print("Elements:", element_1, element_2)

    if element_1 == 0 and element_2 == 9:
        cards_1.append(element_1)
        cards_1.append(element_2)

    elif element_2 == 0 and element_1 == 9:
        cards_2.append(element_1)
        cards_2.append(element_2)

    elif element_1 > element_2:
        cards_1.append(element_1)
        cards_1.append(element_2)

    elif element_2 > element_1:
        cards_2.append(element_1)
        cards_2.append(element_2)

    print("Cards:", cards_1, cards_2)

    if counter > 100:
        break

if not cards_1:
    print('second', cards_2)

else:
    print('first', cards_1)


# Task 4
"""
Даны две непустые очереди.
Элементы каждой из очередей упорядочены по возрастанию.
Объединить очереди в одну с сохранением упорядоченности элементов.
"""

queue1 = [1, 2, 3, 4]
queue2 = [1, 2, 3]


def sort_n_merge(queue_first, queue_second):
    tmp_queue = []
    while queue_second:
        if not queue_first:
            tmp_queue.append(queue_second.pop())
        elif queue_first[-1] > queue_second[-1]:
            tmp_queue.append(queue_first.pop())
        else:
            tmp_queue.append(queue_second.pop())
    while queue_first:
        tmp_queue.append(queue_first.pop())
    return tmp_queue[::-1]


print(sort_n_merge(queue1, queue2))  # [1, 1, 2, 2, 3, 3, 4]
print(sort_n_merge([0, 1, 2, 5, 10], [2, 6, 10]))  # [0, 1, 2, 5, 6, 10]
print(sort_n_merge([1, 3, 5], []))  # [1, 3, 5]
print(sort_n_merge([], [1, 3, 5]))  # [1, 3, 5]
