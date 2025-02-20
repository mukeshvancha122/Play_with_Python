####stack using arrays 

class stack:
    def __init__(self):
        self.stack=[]

    def push(self,element):
        self.stack.append(element)
    
    def pop(self):
        if len(self.stack)==0:
            return "stack empty"
        else:
            return self.stack.pop()
        
    def peek(self):
        if len(self.stack)==0:
            return "stack emplty"
        else :
            return  self.stack[-1]
    def is_empty(self):
        return len(self.stack)==0
    
    def size(self):
        return len(self.stack)
    
    def display(self):
        print(self.stack)

stc=stack()

stc.push(1)
stc.push(2)
stc.push(3)
stc.push(4)
stc.display()
print(stc.pop())
stc.display()
print(stc.peek())
print(stc.is_empty())
print(stc.size())
stc.display()