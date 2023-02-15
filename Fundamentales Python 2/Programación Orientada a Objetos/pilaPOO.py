
class Stack():
    def __init__(self):
        self.stack_list = []
    
    def push(self, val):
        self.stack_list.append(val)
    
    def pop(self):
        val = self.stack_list[-1]
        del self.stack_list[-1]
        return val

pila = Stack()

#for i in range(5):
#    print(i)
#    pila.push(i)
#for i in range (5):
#    print(pila.pop())