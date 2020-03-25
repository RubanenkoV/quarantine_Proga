#Задачу не до конца довёл

num = int(input('Enter number of tests'))
arrs = [[] for _ in range(num)]
ns = []
#k = [0]
#for l in range(num-1):
    #k.append(0)
for i in range(num):
    n = int(input('n'))
    ns.append(n)
    for j in range(n):
        x = int(input())
        arrs[i].append(x)
print(ns[1])
#print(arrs)

def qsort(array, a, b):
    k = 0
    if a >=b:
        k += 1
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
    print(k)
for q in range(num):
    qsort(arrs[q], 0, ns[q] -1)
#print(k)
print(arrs)