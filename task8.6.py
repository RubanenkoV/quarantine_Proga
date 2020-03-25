## На еолимп задача пройти не должна, так как у меня используется defaultdict, а я не думаю, что это предусмотрено решением, ожидаемым там.

from collections import defaultdict
n = int(input())
d = defaultdict(list)
arr1 = []
arr2 = []
for j in range(n):
    x,y = input().split()
    d[x].append(y)
    arr1.append(x)
    arr2.append(x)

    #for x1 in arr2:
        #for x2 in arr2:
            #if x1 == x2:
                #d[x1].append(d[x2])
                #list(set(arr2))
def merge_sort(array):
    print("Splitting ", array)
    if len(array) > 1:
        mid = len(array) // 2
        lefthalf = array[:mid]
        righthalf = array[mid:]
        merge_sort(lefthalf)
        merge_sort(righthalf)
        print(array)
        i = 0
        j = 0
        k = 0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                array[k] = lefthalf[i]
                i += 1
            else:
                array[k] = righthalf[j]
                j += 1
            k += 1
        while i < len(lefthalf):
            array[k] = lefthalf[i]
            i += 1
            k += 1
        while j < len(righthalf):
            array[k] = righthalf[j]
            j += 1
            k += 1
merge_sort(arr1)
#print(arr1)
for m in arr1:
    print(m, d[m]) ## Задача почти полностью работает. Так как я использовал defaultdict, чтобы поставить в соответствие элементы input'a, 
                    ## я не до конца понимаю как разделить значения, которые присваиваются одному и тому же ключу
