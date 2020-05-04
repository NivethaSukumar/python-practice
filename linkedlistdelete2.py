class Node:
    def __init__(self,data):
        self.data=data
        self.next=None  
class Linkedlist:
    def __init__(self):
        self.head=None 
    def push(self,new_data):
        new_node=Node(new_data)
        new_node.next=self.head
        self.head=new_node
    def pop(self,position):
        if self.head is None:
            return None
        temp=self.head
        if(position==0):
            self.head=temp.next
            temp=None 
            return
        for i in range(position-1):
            temp=temp.next
            if temp is None:
                break
        if temp is None:
            return
        if (temp.next) is None:
            return
        next=temp.next.next
        temp.next=None
        temp.next=next
    def printlist(self):
        temp=self.head
        while(temp):
            print(temp.data)
            temp=temp.next
llist=Linkedlist()
llist.push(7)
llist.push(8)
llist.push(9)
llist.push(10)
llist.push(11)
print("Created linked list:")
llist.printlist()
llist.pop(3)
print("After deletion of element at position 3:")
llist.printlist()