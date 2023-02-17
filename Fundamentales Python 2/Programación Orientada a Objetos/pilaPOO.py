
class Stack():
    def __init__(self):
        self.stack_list = []
    
    def push(self, val):
        self.stack_list.append(val)
    
    def pop(self):
        val = self.stack_list[-1]
        del self.stack_list[-1]
        return val

class AddingStack(Stack):
    def __init__(self):
        Stack.__init__(self)
        self.__sum = 0

    def get_sum(self):
        return self.__sum

    def push(self, val):
        self.__sum += val
        Stack.push(self, val)

    def pop(self):
        val = Stack.pop(self)
        self.__sum -= val
        return val


stack_object = AddingStack()

#print(stack_object.__dict__)

#for i in range(5):
#    stack_object.push(i)
#print(stack_object.get_sum())
#for i in range(5):
#    print(stack_object.pop())    