def get_hash(key):
    h = 0
    for char in key:
        h+=ord(char)
    return h % 100

class Hashtable:
    def __init__(self):
        self.max = 20
        self.arr = [None for i in range(self.max)]
    def get_hash(self,key):
        h = 0
        for char in key:
            h+=ord(char)
        return h % self.max
    
    def __setitem__(self,key,val):
        h = self.get_hash(key)
        return self.arr[h]

    def __getitem__(self,key):
        chave = get_hash(key)
        return self.arr[chave]
    
    def __delitem__(self,key):
        h = self.get_hash(key)
        self.arr[h] = None
        
    def print(self):
        print(self.arr)
t = Hashtable()
t.__setitem__('march 6','1202')
t.print()




# def get_hash(key):
#     h = 0
#     for char in key:
#         h+=ord(char)
#     return h % 100

# class Hashtable:
#     def __init__(self):
#         self.max = 20
#         self.arr = [[] for i in range(self.max)]
#     def get_hash(self,key):
#         h = 0
#         for char in key:
#             h+=ord(char)
#         return h % self.max
    
#     def __setitem__(self,key,val):
#         h = self.get_hash(key)
#         for idx,element in enumerate(self.arr[h]):
#             if len(element) == 2 and element[0]== key:
#                 self.arr[h][idx] = (key,val)
#                 found = True
#                 return
#         self.arr[h].append((key,val))

#     def __getitem__(self,key):
#         h = self.get_hash(key)
#         for element in self.arr[h]:
#             if element[0] == key:
#                 return element[1]
#         return None
    
#     def __delitem__(self,key):
#         h = self.get_hash(key)
#         for index , element in enumerate(self.arr[h]):
#             if element[0] == key:
#                 del self.arr[h][index]
#                 return
#         return None
#     def print(self):
#         print(self.arr)
# t = Hashtable()
# t.__setitem__('march 6','1')
# t.__setitem__('march 2','12')
# t.__setitem__('march 10','982')
# t.__setitem__('march 12','982')
# t.print()
# print(t.__getitem__('march 6'))
# t.__delitem__('march 6')
# t.print()




