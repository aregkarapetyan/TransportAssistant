'''
Created by Areg Karapetyan
'''

class QueueArray:
    def __init__(self,size):
        # Create empty deque and fill with 'None' using the given size of the list
        self.deque = []
        for i in range(size):
            self.deque.append(None)

    def add(self,NewVal):
        # Add new element to the queue
        for i in range(len(self.deque)):
            if self.deque[i] is None:
                self.deque[i]=NewVal
                return
        self.resize()
        last_index=int(len(self.deque)/2)
        self.deque[last_index]=NewVal

    def remove(self):
        # Remove the first element of the queue
        self.deque.pop(0)
        self.deque.append(None)

    def first(self):
        # Returns the first element of the queue
        return self.deque[0]

    def last(self):
        # Returns the last non-"None" element of the queue
        l_index = self.last_index()
        return self.deque[l_index]

    def last_index(self):
        # Returns the index of the last non-"None" element of the queue
        for i in range(len(self.deque)):
            if self.deque[i] is None:
                return i-1
        return len(self.deque)-1

    def resize(self):
        # Resizes the queue after the size limit is reached by adding "None" elements, so that the deque will double its size
        b = []
        for i in range(len(self.deque)):
            b.append(None)
        self.deque = self.deque + b

    def print_deq(self):
        # Prints the deque
        print (self.deque)