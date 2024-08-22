# Rotate List

# a = [1,2,3,4,5]
# k = 3
# l= a[k:] + a[:k]

# print(l)    

# linked list

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class linkedlist:
    def __init__(self):
        self.head = None

    def append(self,data):
        newnode = Node(data)
        if not self.head: # linked list is empty
            self.head  = newnode
            return

        lastnode = self.head

        while lastnode.next:
            lastnode = lastnode.next
        lastnode.next = newnode

    def prepend(self,data):
        newnode = Node(data)
        newnode.next = self.head
        self.head = newnode

    def delete(self,key):
        currentnode = self.head
        if currentnode and currentnode.data == key:
            self.head = currentnode.next
            currentnode = None
            return

        prev = None
        while currentnode and currentnode.data != key:
            prev = currentnode
            currentnode = currentnode.next

        if currentnode is None:
            return

        prev.next = currentnode.next
        currentnode =  None

    def rotate(self,key):
        if not self.head or key==0:
            return
        
        lastnode = self.head
        length = 1

        while lastnode.next:
            lastnode = lastnode.next
            length += 1

        lastnode.next = self.head # making a circular list

        key = key % length # if key > length in terms of circular list
        skiplength = length-key
        newlastnode = self.head

        for _ in range(skiplength-1):
               newlastnode = newlastnode.next

        self.head = newlastnode.next
        newlastnode.next = None        


    def print(self):
        currentnode = self.head
        while currentnode:
            print(currentnode.data,end="->")
            currentnode = currentnode.next

        print("None")


list = linkedlist()
list.append(1)
list.append(2)
list.append(3)
list.append(4)
list.prepend(0)
list.print()
list.delete(1)
list.print()
list.rotate(3) # 3 means linked list rotates 3 times
list.print()