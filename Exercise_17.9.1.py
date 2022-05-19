array = list(map(int,input('Введите числа через пробел от 0 до 100: ').split()))

print(array)
for i in range(len(array)):  # проходим по всему массиву
    idx_min = i  # сохраняем индекс предположительно минимального элемента
    for j in range(i, len(array)):
        if array[j] < array[idx_min]:
            idx_min = j
    if i != idx_min:  # если индекс не совпадает с минимальным, меняем
        array[i], array[idx_min] = array[idx_min], array[i]
print(array)

def binary_search(array, element,  left, right):
    if  left > right:
        return "Число не найдено"
    middle = (left + right) // 2
    if array[middle] == element:
        return  middle
    if element < array[middle]:
        return binary_search(array, element, left, middle-1)
    else:
        return binary_search(array, element, middle+1, right)

while True:
    try:
        element = int(input('Введите число от 0 до 100: '))

        if element <=0 or element >= 100:
            raise Exception
        break
    except ValueError:
       print('Ввести число!')
    except Exception:
       print('Неверный диапазон!')

print(binary_search(array, element, 0, len( array)))
