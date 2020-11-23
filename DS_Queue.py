'''
Created by Areg Karapetyan
'''

class QueueArray:
    def __init__(self,size):
        # Create empty queue and fill with 'None' using the given size of the list
        self.queue = []
        for i in range(size):
            self.queue.append(None)

    def add(self,NewVal):
        # Add new element to the queue
        for i in range(len(self.queue)):
            if self.queue[i] is None:
                self.queue[i]=NewVal
                return
        self.resize()
        last_index=int(len(self.queue)/2)
        self.queue[last_index]=NewVal

    def remove(self):
        # Remove the first element of the queue
        self.queue.pop(0)
        self.queue.append(None)

    def first(self):
        # Returns the first element of the queue
        return self.queue[0]

    def last(self):
        # Returns the last non-"None" element of the queue
        l_index = self.last_index()
        return self.queue[l_index]

    def last_index(self):
        # Returns the index of the last non-"None" element of the queue
        for i in range(len(self.queue)):
            if self.queue[i] is None:
                return i-1
        return len(self.queue)-1

    def resize(self):
        # Resizes the queue after the size limit is reached by adding "None" elements, so that the queue will double its size
        b = []
        for i in range(len(self.queue)):
            b.append(None)
        self.queue = self.queue + b

    def print_deq(self):
        # Prints the queue
        print (self.queue)