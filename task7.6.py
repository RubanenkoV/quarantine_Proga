n = int(input())
arr = []
for i in range(n):
    i = input()
    arr.append(i)
def bubble_sort(array):
    n = len(array)
    for pass_num in range(n-1,0,-1):
        for j in range(pass_num):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]

bubble_sort(arr)
for k in arr:
    print(k)
