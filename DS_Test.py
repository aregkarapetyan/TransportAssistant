'''
Created by Areg Karapetyan

Used to test All Data Structures
'''

from DS_Single_Linked_List import *
from DS_Double_Linked_List import *
from DS_Stack import *
from DS_Queue import *
from DS_Deq import *
from DS_HashMap import *
from DS_HashSet import *

print("----------------------------------------------------")
print("Choose number to check your desired data structure"
      "\n 1.Single Linked List"
      "\n 2.Double Linked List"
      "\n 3.Stack"
      "\n 4.Queue"
      "\n 5.Deque"
      "\n 6.HashMap"
      "\n 7.HashSet")

def choice():
    choice = input("Input here: ")

    if choice == "1":
        '''
        Tests for Single Linked List
        '''
        List_L = SLinkedList()
        List_L.AtBeginning("Mon")
        List_L.AtEnd("Tue")
        List_L.AtEnd("Wed")
        List_L.AtEnd("Fri")
        List_L.InsertAfter(List_L.HeadVal.NextVal.NextVal, "Thu")
        List_L.ListPrint()
        print("----------------")
        List_L.RemoveNode("Mon")
        List_L.ListPrint()
        print("First element is: ", List_L.FirstElem())
        print("Last element is: ", List_L.LastElem())
        print("Size is: ", List_L.Size())
    elif choice == "2":
        '''
        Tests for Double Linked List
        '''
        dll_test = DLinkedList()
        dll_test.addFirst("Mars")
        dll_test.addLast("Jupiter")
        dll_test.addFirst("Venus")
        dll_test.addLast("Saturn")
        dll_test.addFirst("Mercury")
        dll_test.addFirst("Sun")
        dll_test.addLast("Uranus")
        dll_test.addLast("Neptune")
        print("--------Initial Linked List--------")
        dll_test.listprint()
        print("-----------------------------------")

        dll_test.RemoveFirst()
        dll_test.InsertAfter(dll_test.HeadVal.NextVal,"Earth")
        dll_test.RemoveLast()
        dll_test.RemoveNode("Mars")

        print("--------Linked list after removing first and last elements, removing 'Mars' and adding 'Earth'--------")
        dll_test.listprint()
        print("--------First and last elements right now--------")
        print(dll_test.First())
        print(dll_test.Last())
        print("--------Size right now--------")
        print(dll_test.Size())
    elif choice == "3":
        '''
            Tests for Stack
        '''
        stack_test = Stack()
        print("--------Initial stack--------")
        stack_test.AddElem("Mercury")
        stack_test.AddElem("Venus")
        stack_test.AddElem("Earth")
        stack_test.PrintStack()
        print("--------Stack after removing element--------")
        stack_test.RemoveElem()
        stack_test.PrintStack()
        print("Top element of the stack is: ", stack_test.TopElem())
        print("Size of the stack: ", stack_test.Size())
    elif choice == "4":
        '''
        Tests for Queue
        '''
        queue_test = QueueArray(3)  # Size = 3
        print("--------Initial queue--------")
        queue_test.add("Mercury")
        queue_test.add("Venus")
        queue_test.add("Earth")
        queue_test.add("Mars")
        queue_test.print_deq()
        print("--------Final queue--------")
        queue_test.remove()
        queue_test.print_deq()
        print("First element is: ", queue_test.first())
        print("Last element is: ", queue_test.last())
    elif choice == "5":
        '''
            Tests for Deque
        '''
        deq_test = DequeArray(3)  # size = 3
        deq_test.addFirst("Tue")
        deq_test.addFirst("Mon")
        deq_test.addLast("Wed")
        deq_test.addLast("Thu")
        deq_test.addLast("Fri")

        deq_test.print_deq()
        print(deq_test.last())
        deq_test.removeLast()
        deq_test.removeFirst()
        deq_test.print_deq()
        print("First element is: ", deq_test.first())
        print("Last element is: ", deq_test.last())
        print("Last non-None index is: ", deq_test.last_index())
    elif choice == "6":
        '''
        Tests for HashMap
        '''
        addressBook = HashMap()
        addressBook.put("Armen", {"fullName": "Armen Hakobyan",
                                  "phoneNumber": "094444444"})
        addressBook.put("Artak", {"fullName": "Artak Zakaryan",
                                  "phoneNumber": "094444441"})
        addressBook.put("Ani", {"fullName": "Ani Aslanyan",
                                "phoneNumber": "094444442"})
        addressBook.put("Karen", {"fullName": "Karen Kocharyan",
                                  "phoneNumber": "094444445"})
        addressBook.put("Zaven", {"fullName": "Zaven Hakobyan",
                                  "phoneNumber": "094444447"})
        addressBook.put("Gohar", {"fullName": "Gohar Vardanyan",
                                  "phoneNumber": "094444454"})

        print("---------Initial Address Book---------")
        for elem in addressBook:
            print(elem.get("fullName"))

        print()
        addressBook.remove("SthNotInTheAddressBook")
        addressBook.remove("Zaven")
        print("")
        print("---------Updated Address Book---------")
        for elem in addressBook:
            print(elem.get("fullName"))

        print()
        print("---------Checking if key is present---------")
        addressBook.hasKey("Armen")
        addressBook.hasKey("SthRandom")
        print()
        print("---------Size of HashMap---------")
        print(addressBook.size())
    elif choice == "7":
        '''
            Tests for HashSet
        '''
        HS = HashSet(5)
        print("---------Hashing of elements---------")
        HS.add("Tokyo")
        HS.add("Rio")
        HS.add("Nairobi")
        HS.add("Moscow")
        HS.add("Berlin")
        HS.add("Stockholm")
        HS.add("Helsinki")
        HS.add("Oslo")
        HS.add("Denver")
        HS.add("Lisbon")
        print("---------Elements of HashSet---------")
        HS.print()
        print("---------HashSet current size---------")
        print(HS.size())
        HS.remove("Moscow")
        HS.remove("Rio")
        print("---------HashSet after removing Moscow---------")
        HS.print()
        print("---------HashSet current size---------")
        print(HS.size())
    else:
        print("Input number between 1 and 7")
        choice()
choice()