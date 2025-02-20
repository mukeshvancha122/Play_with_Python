class node:
    def __init__(self,data):
        self.data=data
        self.next=None
    
class stack:
    def __init__(self):
        self.head=None
        self.size=0
    
    def push(self,data):
        new_node=node(data)
        if self.head:
            new_node.next=self.head
        self.head=new_node
        self.size+=1
    
    def pop(self):
        if self.size==0:
            return "empty stack "
        popper=self.head
        self.head=self.head.next
        self.size-=1
        return popper.data
    def peek(self):
        if self.size==0:
            return "empty stack"
        return self.head.data
    def is_empty(self):
        return self.size==0
    
    def esize(self):
        return self.size
    

stc=stack()
stc.push(1)
stc.push(2)
stc.push(3)
print(stc.pop())
print(stc.peek())
print(stc.is_empty())
print(stc.esize())
print(stc.pop())
print(stc.pop())
print(stc.pop())
