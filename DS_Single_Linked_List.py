'''
Created by Areg Karapetyan
'''

class Node:
    # Class to create nodes for linked list
    def __init__(self,DataVal=None):
        self.DataVal = DataVal
        self.NextVal = None

class SLinkedList:
    #Class to create linked list
    def __init__(self):
        self.HeadVal = None

    def ListPrint(self):
        # Prints the linked list
        PrintVal = self.HeadVal
        while PrintVal is not None:
            print(PrintVal.DataVal)
            PrintVal = PrintVal.NextVal

    def FirstElem(self):
        #   Returns the first element of the linked list
        return self.HeadVal.DataVal

    def LastElem(self):
        #   Returns the last element of the linked list
        last = self.HeadVal
        while last is not None:
            if last.NextVal == None:
                return (last.DataVal)
            last = last.NextVal

    def AtBeginning(self,NewData):
        # Adds new elements at the beginning of the linked list
        NewNode = Node(NewData)
        NewNode.NextVal = self.HeadVal
        self.HeadVal = NewNode

    def AtEnd(self,NewData):
        # Adds new elements at the end of the linked list
        NewNode = Node(NewData)
        if self.HeadVal is None:
            self.HeadVal = NewNode
            return
        LastElem = self.HeadVal
        while(LastElem.NextVal is not None):
            LastElem = LastElem.NextVal
        LastElem.NextVal=NewNode

    def InsertAfter(self,middle_node,NewData):
        # Adds new elements in the list after the middle node
        if middle_node is None:
            print("Error. Mentioned node is absent")
            return
        NewNode = Node(NewData)
        NewNode.NextVal = middle_node.NextVal
        middle_node.NextVal = NewNode

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
        #   Removes the first element of the linked list
        self.RemoveNode(self.FirstElem())

    def RemoveLast(self):
        #   Removes the last element of the linked list
        self.RemoveNode(self.LastElem())

    def IndexOf(self,node):
        #   Returns the index of the needed element of the linked list
        elem = self.HeadVal
        index = 0
        while elem is not None:
            if elem.DataVal == node:
                return index
            elem = elem.NextVal
            index += 1

    def Size(self):
        #   Returns the size of the linked list
        size = 1
        elem = self.HeadVal
        if elem == None:
            return 0
        while elem is not None:
            if elem.NextVal == None:
                return size
            elem = elem.NextVal
            size += 1