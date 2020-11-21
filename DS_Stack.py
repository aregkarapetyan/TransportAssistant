'''
Created by Areg Karapetyan
'''

class Stack:
    def __init__(self):
        self.Stack = []

    def AddElem(self,DataVal):
        #   Adds element to the stack
        if DataVal not in self.Stack:
            self.Stack.append(DataVal)
            return True
        else:
            return False

    def RemoveElem(self):
        #   Removes element from the stack
        if len(self.Stack) <= 0:
            return "Stack is empty"
        else:
            return self.Stack.pop()

    def TopElem(self):
        #   Returns top element to the stack
        return self.Stack[-1]

    def IsEmpty(self):
        #   Checks if the stack is empty
        if len(self.Stack) == 0:
            return True
        else:
            return False

    def Size(self):
        #   Returns the size of the stack
        return len(self.Stack)

    def PrintStack(self):
        #   Print elements of the stack
        for i in range(len(self.Stack)):
            print(self.Stack[i])