class node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None

node1=node(1)
node2=node(2)
node3=node(3)

node1.next=node2
node2.next=node3

node2.prev=node1
node3.prev=node2

current=node1
while current:
    print(current.data)
    current=current.next
    print("address",current)


##backward
current=node3
while current:
    print(current.data)
    current=current.prev
    print("address",current)