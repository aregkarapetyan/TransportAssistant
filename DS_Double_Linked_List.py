'''
Created by Areg Karapetyan
'''

class Node:
    # Class to create nodes for linked list
    def __init__(self,DataVal=None):
        self.DataVal = DataVal
        self.NextVal = None
        self.PrevVal = None

class DLinkedList:
    last = None     #to keep the last element

    def __init__(self):
        self.HeadVal= None

    def listprint(self):
        node = self.HeadVal
        # Prints the linked list
        while node is not None:
            print(node.DataVal),
            node = node.NextVal

    def addFirst(self,NewData):
        # Adds new element to the beginning of the list
        NewNode = Node(NewData)
        NewNode.NextVal = self.HeadVal
        if self.HeadVal is None:
            self.last = NewNode
        if self.HeadVal is not None:
            self.HeadVal.PrevVal = NewNode
        self.HeadVal = NewNode

    def addLast(self, NewData):
        # Adds new element to the end if the list
        NewNode = Node(NewData)
        NewNode.NextVal = None
        if self.HeadVal is None:
            NewNode.PrevVal = None
            self.HeadVal = NewNode
            return
        last = self.HeadVal
        while (last.NextVal is not None):
            last = last.NextVal
        last.NextVal = NewNode
        NewNode.PrevVal = last
        self.last = NewNode
        return

    def InsertAfter(self, PrevNode, NewData):
        #   Inserts new element after the given element
        if PrevNode is None:
            return
        NewNode = Node(NewData)
        NewNode.NextVal = PrevNode.NextVal
        PrevNode.NextVal = NewNode
        NewNode.PrevVal = PrevNode
        if NewNode.NextVal is not None:
            NewNode.NextVal.PrevVal = NewNode

    def InsertBefore(self, NextNode, NewData):
        #   Inserts new element before the given element
        if NextNode is None:
            return
        NewNode = Node(NewData)
        NewNode.PrevVal = NextNode.PrevVal
        NextNode.PrevVal = NewNode
        NewNode.NextVal = NextNode
        if NewNode.NextVal is not None:
            NewNode.PrevVal.NextVal = NewNode

    def RemoveNode(self, RemoveKey):
        # Removes an elements from linked list using the provided remove key
        HeadVal = self.HeadVal

        if HeadVal is not None:
            if HeadVal.DataVal == RemoveKey:
                self.HeadVal = HeadVal.NextVal
                HeadVal = None
                return
        while HeadVal is not None:
            if HeadVal.DataVal == RemoveKey:
                break
            prev = HeadVal
            HeadVal = HeadVal.NextVal
        if HeadVal == None:
            return
        prev.NextVal = HeadVal.NextVal

        HeadVal = None

    def RemoveFirst(self):
        #   Removes the first element of the list
        self.RemoveNode(self.First())

    def RemoveLast(self):
        #   Removes the last element of the list
        self.RemoveNode(self.last.DataVal)
        self.last = self.last.PrevVal

    def First(self):
        #   Returns the first element of the list
        return self.HeadVal.DataVal

    def Last(self):
        #   Returns the last element of the list
        return self.last.DataVal

    def IndexOf(self,node):
        #   Returns the index of the needed element of the list
        elem = self.HeadVal
        index = 0
        while elem is not None:
            if elem.DataVal == node:
                return index
            elem = elem.NextVal
            index += 1

    def Size(self):
        #   Returns the size of the list
        size = 1
        elem = self.HeadVal
        if elem == None:
            return 0
        while elem is not None:
            if elem.NextVal == None:
                return size
            elem = elem.NextVal
            size += 1