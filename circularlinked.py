class node:
    def __init__(self,data):
        self.data=data
        self.next=None

node1=node(1)
node2=node(2)
node3=node(3)

node1.next=node2
node2.next=node3
node3.next=node1

current=node1
startnode=node1

while current:
    print(current.data)
    current=current.next
    print("address",current)
    if current==startnode:
        print("circular linked list" , current.data)
        break
