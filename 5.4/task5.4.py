class HashTable:

    def __init__(self):
        self.max_size = 100000
        self.current_size = 0
        self.keys = [None]*self.max_size
        self.values = [None]*self.max_size

    def hash(self, key):
        s = 0
        for c in key:
            s = s*31 + ord(c)
        return s%self.max_size

    def put(self, key, value):
        current  = self.hash(key)
        while self.keys[current] != None:
            if self.keys[current] == key:
                self.values[current] = value
                return
            current += 1
        self.keys[current] = key
        self.values[current] = value
        self.current_size += 1

    def get(self, key):
        current = self.hash(key)
        while self.keys[current] != None:
            if self.keys[current] == key:
                return self.values[current]
            current += 1
        return None

    def __setitem__(self, key, value):
        self.put(key, value)

    def __getitem__(self, key):
        return self.get(key)

    def __len__(self):
        return self.current_size

    def __contains__(self, key):
        return not (self[key] is None)

    def __str__(self):
        return str(self.keys) + '\n' + str(self.values) + '\n'

words = HashTable()
test = []
file = open("input1.txt", "r")
for i in file:
    w = i.split()
    #print(w)
    for j in range(len(w)):
        w[j] = w[j].replace(',', '')
        w[j] = w[j].replace('.', '')
        w[j] = w[j].replace(':', '')
        w[j] = w[j].replace('"', '')
        w[j] = w[j].replace('D', 'd')
        w[j] = w[j].replace('L', 'l')
        w[j] = w[j].replace('A', 'a')
        w[j] = w[j].replace('T', 't')
        w[j] = w[j].replace('S', 's')
	#Это для данного примера. Для универсальности можно весь алфавит под replace написать)
        if w[j] in words:
            pass
        else:
            words.put(w[j], w[0])
            #print(words)
            test.append(w[j])
file.close()
test = sorted(test)
#print(test)
test.sort()
file1 = open("output1.txt", "w")
file1.write('\n')
for i in range(len(words)):
    file1.write(test[i])
    file1.write('\n')
file1.close()

