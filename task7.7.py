#Не думаю, что до конца понял, что нужно было реализовать в выводе, но алгоритм сортировки ставкой работает правильно

n = int(input())
arr = []
for i in range(n):
    i = int(input())
    arr.append(i)

def insertion_sort(array):
    n = len(array)
    for index in range(1, n):
        CurrentValue = array[index]
        position = index
        while position > 0:
            if array[position - 1] > CurrentValue:
                array[position] = array[position - 1]
            else:
                break
            position -= 1

        array[position] = CurrentValue

insertion_sort(arr)
print(arr)
