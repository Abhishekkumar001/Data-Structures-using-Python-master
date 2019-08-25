class Stack:
    def __init__(self):
        self.stk=[]
    def push(self,x):
        self.stk.append(x)
    def pop(self):
        if self.stk==[]:
            return -1
        else:
            return self.stk.pop()
    def peep(self):
        n=len(self.stk)
        return self.stk[n-1]
    def display(self):
        return self.stk