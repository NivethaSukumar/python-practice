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
    def pop(self,key):
        temp=self.head
        if(temp is not None):
            if(temp.data==key):
                self.head=temp.next
                temp=None
                return
        while(temp is not None):
            if(temp.data==key):
                break
            prev=temp
            temp=temp.next
        if(temp==None):
            return
        prev.next=temp.next
        temp==None
    def printlist(self):
        temp=self.head
        while(temp):
            print(temp.data)
            temp=temp.next
llist=Linkedlist()
llist.push(1)
llist.push(2)
llist.push(3)
llist.push(4)
llist.push(5)
print("Created Linked list")
llist.printlist()
llist.pop(1)
print("After deletion of key 1:")
llist.printlist()
llist.pop(3)
print("After deletion of key 3:")
llist.printlist()
llist.pop(5)
print("After deletion of key 5:")
llist.printlist()