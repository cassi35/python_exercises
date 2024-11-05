
# Detect loop or cycle in a linked list

def delete():
    class Node:
        def __init__(self,value):
            self.data = value
            self.next = None
    class LinkedList:
        def __init__(self):
            self.head = None
        def append(self,value):
            if self.head is None:
                self.head = Node(value)
            else:
                temp = self.head
                while(temp.next):
                    temp = temp.next
                temp.next = Node(value)
        def detect_loop(self):
            st = set()
            temp = self.head
            while(temp != None):
                if temp != None:
                    return True
                st.add(temp)
                temp = temp.next 
            return False
        def reverse(self,temp):
            if temp == None:
                return
            else:
                 
                self.reverse(temp.next)
                print(temp.data)
        
    lists = LinkedList()
    lists.append(1)
    lists.append(2)
    lists.append(3)
    lists.append(4)
    lists.reverse(lists.head)
delete()