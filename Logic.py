#Sorting a list of elements
def srt (self, key = None, reverse = False):
    if key == None:
        key = lambda x : x
    if reverse:
        for i in range(len(self)-1):
            for j in range(i + 1, len(self)):
                if key(self[i]) < key(self[j]):
                    self[i], self[j] = self[j], self[i]
    else:
        for i in range(len(self)-1):
            for j in range(i + 1, len(self)):
                if key(self[i]) > key(self[j]):
                    self[i], self[j] = self[j], self[i]
    return self
#Filter a list of elements
#maleu mama si maicuta mea
def filter(self, key = None):
    if key == None:
        key = lambda x : x
    return [x for x in self if key(x)]

if __name__ == "__main__":
    print(srt([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], reverse = True))
    print(filter([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], key = lambda x : x % 2 == 0))