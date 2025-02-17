class node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
def traverse(head):
    current = head
    while current :
        print(current.data)
  
        current=current.next

def low(head):
    min=head
    current=head.next
    while current:
        if current.data<min.data:
            min=current.data
        current=current.next
    return min.data

def delete(head,todel):
    if head.data==todel.data:
        return head.next

    current=head
    while current and current.next!=todel:
        current = current.next 
    
    if current==None:
        return head
    
    current.next= current.next.next

    return head


def insertbegin(head,data):
    print("inserting at begin")
    newnode=node(data)
    newnode.next=head
    return newnode
##insert at specific position 

def insert1(head,data,pos):
    if pos==0:
        return insertbegin(head,data)
    newnode = node(data)
    current=head
    for _ in range(pos-1):
        if current == None or current.next==None:
            print("out of range")
            return head
        current=current.next    

    newnode.next=current.next
    current.next=newnode
    return head


node1 = node(12)
node2 = node(99)
node3 = node(37)
node1.next = node2
node2.next = node3

traverse(node1)
print(low(node1))
node1=delete(node1,node2)

print("after delete")
traverse(node1)

node1=insert1(node1,100,4)

print("after insert")
traverse(node1)
