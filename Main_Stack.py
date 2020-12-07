'''
Created by Areg Karapetyan
'''

from Main_Stack_Functionality import *

def main():
    print ("<-<-<-<-< Welcome to Transport assistant >->->->->")
    origin = input("Input your origin point: ")
    destination = input("Input your destination point: ")
    UserInput = BusStreets(origin, destination)

    bus_str_stack = UserInput.create_stack()
    print("")
    valid_transport, valid_indexs = UserInput.search_in_stack(origin, destination, bus_str_stack)
    if len(valid_transport)>0:
        UserInput.get_valid_transport_string(valid_transport)
        if len(valid_transport) > 1:
            UserInput.find_shortest(valid_transport, valid_indexs)
    else:
        print("No valid transport for your desired streets")
main()