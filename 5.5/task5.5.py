with open('input2.txt', 'r', encoding="Cp1252") as inputfile:
    f = inputfile.readlines()
sp = []
for i in f:
    sp.append(i)
    
word = sp[0]
N = int(sp[1])
words = []
for i in range(2, N + 2):
    words.append(sp[i])

def length(s, b):
    k = 0
    for i in range(len(s)):
        if s[i] == b:
            k += 1
    return k

for wrds in words:
    for j in range(len(wrds)):
        if length(wrds, wrds[j]) > length(word, wrds[j]):
            N -= 1
            break

file1 = open("output2.txt", "w")
file1.write(str(N))
file1.close()
