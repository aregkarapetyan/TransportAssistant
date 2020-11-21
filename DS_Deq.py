'''
Created by Areg Karapetyan
'''

class DequeArray:
    def __init__(self,size):
        # Create empty deque and fill with 'None' using the given size of the list
        self.deque = []
        for i in range(size):
            self.deque.append(None)

    def addFirst(self,NewVal):
        # Add new element at the beginning of the deque
        if self.deque[0] is None:
            self.deque[0]=NewVal
        elif self.deque[-1] is None:
            a = 1%len(self.deque)
            self.deque = self.deque[-a:]+self.deque[:-a]
            self.deque[0] = NewVal
        else:
            self.resize()
            a = 1 % len(self.deque)
            self.deque = self.deque[-a:] + self.deque[:-a]
            self.deque[0] = NewVal

    def addLast(self,NewVal):
        # Add new element to the end of the deque
        for i in range(len(self.deque)):
            if self.deque[i] is None:
                self.deque[i]=NewVal
                return
        self.resize()
        last_index=int(len(self.deque)/2)
        self.deque[last_index]=NewVal

    def removeFirst(self):
        # Remove the first element of the deque
        self.deque.pop(0)
        self.deque.append(None)

    def removeLast(self):
        # Remove the last element of the deque
        last_index = self.last_index()
        self.deque[last_index]=None

    def first(self):
        # Returns the first element of the deque
        return self.deque[0]

    def last(self):
        # Returns the last non-"None" element of the deque
        l_index = self.last_index()
        return self.deque[l_index]

    def last_index(self):
        # Returns the index of the last non-"None" element of the deque
        for i in range(len(self.deque)):
            if self.deque[i] is None:
                return i-1
        return len(self.deque)-1

    def resize(self):
        # Resizes the deque after the size limit is reached by adding "None" elements, so that the deque will double its size
        b = []
        for i in range(len(self.deque)):
            b.append(None)
        self.deque = self.deque + b

    def print_deq(self):
        # Prints the deque
        print (self.deque)