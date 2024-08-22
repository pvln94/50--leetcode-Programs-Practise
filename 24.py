# Intersection of 2 Linked Lists

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data, end="->")
            temp = temp.next
        print("None")  # To indicate the end of the list

    def get_length(self):
        length = 0
        current = self.head
        while current:
            length += 1
            current = current.next
        return length

def get_length(node):
    length = 0
    while node:
        length += 1
        node = node.next
    return length  

def get_intersection_node(headA, headB):
    if not headA or not headB:
        return None
    
    lenA = get_length(headA)
    lenB = get_length(headB)

    while lenA > lenB:
        headA = headA.next
        lenA -= 1 

    while lenB > lenA:
        headB = headB.next
        lenB -= 1

    while headA and headB:
        if headA == headB:
            return headA   
        headA = headA.next
        headB = headB.next
    
    return None

def create_intersecting_lists():
    list1 = LinkedList()
    list2 = LinkedList()

    list1.push(1)
    list1.push(2)
    list1.push(3)

    list2.push(4)
    list2.push(5)

    # Create intersecting node
    intersecting_node = Node(6)
    intersecting_node.next = Node(7)

    # Connect both lists to the intersecting node
    list1.head.next.next.next = intersecting_node
    list2.head.next.next = intersecting_node

    return list1, list2

# Example usage
list1, list2 = create_intersecting_lists()

print("List 1:")
list1.print_list()

print("List 2:")
list2.print_list()

# Find intersection
intersection_node = get_intersection_node(list1.head, list2.head)
if intersection_node:
    print(f"Intersection at node with value: {intersection_node.data}")
else:
    print("No intersection")
