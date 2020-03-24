n = int(input("Number of ropes")) # <--- Приберіть текст в інпуті, E-Olymp на це скаржиться 
k = int(input("Number of houses")) # <--- --//--
#arr = [int(input()) for i in range(n)]
l =[]
i = 0
while i < n:
    x = int(input())
    l.append(x)
    i += 1
l.sort()
#print("------")
left = 0
right = min(l)
a = []
for z in l:
    j = right
    while j >= 0:
        y = 0
        y += z//j
        #print(y)
        if y == k:
            a.append(j)
            #print(a)
        else:
            i -= 1
while left < right:
    mid = (left + right)//2
    #print(mid)
    if max(a) < mid:
        right = mid
    else:
        left = mid
print(max(a))
