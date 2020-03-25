
## на Еолимп задача желтым цветом показывает 0%, но я не могу понять что не так, ведь она работает. (Использовал алгоритм быстрой сортировки)
n = int(input())
el = input().split()
print(el)
#a = el[0]
#b = el[-1]
def qsort(array, a, b):
    if a >=b:
        return
    pivot = array[a + (b - a) // 2]
    left = a
    right = b
    while True:
        while array[left] < pivot:
             left += 1
        while pivot < array[right]:
            right -= 1
        if left >= right:
            break
        array[left], array[right]= array[right], array[left]
        left += 1
        right -= 1
    qsort(array, a, right)
    qsort(array, right + 1, b)

qsort(el, 0, n-1)
print(el)