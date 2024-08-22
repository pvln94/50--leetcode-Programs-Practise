# Linked List cycle

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Linkedlist:
    def __init__(self):
        self.head = None

    def push(self,data):
        newnode = Node(data)
        newnode.next = self.head
        self.head = newnode

    def printlist(self):
        temp = self.head
        while(temp):
            print(temp.data,end=" ")
            temp = temp.next

    def detectloop(self):
        s = set()
        temp = self.head
        while (temp):
            if(temp in s):
                return True
            s.add(temp)
            temp = temp.next

        return False


llist= Linkedlist()
llist.push(1)
llist.push(2)
llist.push(3)
llist.push(4)
llist.head.next.next.next.next = llist.head

if(llist.detectloop()):
    print("Loop Found")
else:
    print("No Loop ")
