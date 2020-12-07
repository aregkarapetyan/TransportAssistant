'''
Created by Areg Karapetyan
'''

from Main_Single_Linked_List_Functionality import *

def main():
    print ("<-<-<-<-< Welcome to Transport assistant >->->->->")
    origin = input("Input your origin point: ")
    destination = input("Input your destination point: ")
    UserInput = BusStreets(origin, destination)

    bus_str_LL=UserInput.create_linked_list()
    valid_transport, valid_indexs = UserInput.search_street_SLL(origin, destination, bus_str_LL)
    if len(valid_transport)>0:
        UserInput.get_valid_transport_string(valid_transport)
        if len(valid_transport) > 1:
            UserInput.find_shortest(valid_transport, valid_indexs)
    else:
        print("No valid transport for your desired streets")


main()