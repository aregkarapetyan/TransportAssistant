'''
Created by Areg Karapetyan
'''

from Main_Data import *
from DS_Stack import *

class BusStreets:
    last_bus_id = 15 # ID of our last bus in data base

    def __init__(self,origin,destination):
        self.origin = origin
        self.destination = destination

    # Search for the origin and destination
    # Get valid transport which includes both origin and destination
    # Get index of each street in the list
    def search_in_stack(self,origin, destination, bus_str_stack):
        valid_transport = []
        valid_indexs = []
        stack_temp = bus_str_stack
        bus_id = self.last_bus_id
        while stack_temp.IsEmpty() is False:
            valid = 0
            street_id = stack_temp.TopElem().Size()
            found_locations = []
            while stack_temp.TopElem().IsEmpty() is False:
                if bus_str_stack.TopElem().TopElem() == str(origin) or bus_str_stack.TopElem().TopElem() == str(destination):
                    valid = valid + 1
                    found_locations.append(street_id)
                street_id = street_id - 1
                stack_temp.TopElem().RemoveElem()
            if valid == 2:
                valid_transport.append(bus_id)
                valid_indexs.append(found_locations)
            bus_id = bus_id - 1
            stack_temp.RemoveElem()
        return valid_transport, valid_indexs

    # Finds shortest route out of all routes (counts number of streets between origin and destination)
    def find_shortest(self, valid_transport, valid_index):
        difference = []
        for i in range(len(valid_index)):
            diff = valid_index[i][1] - valid_index[i][0]
            difference.append(diff)
        try:
            min_index = difference.index(min(difference))
            fastest_transport = valid_transport[min_index]
        except Exception as e:
            fastest_transport = "NONE"
        print("Bus which will help you get from " + self.origin + " to " + self.destination + " in the shortest time is #" + str(fastest_transport))
        return fastest_transport

    #convert list of valid transports to string for user-friendly display
    def get_valid_transport_string(self, valid_transport):
        valid_transport_str = ''
        for i in range(len(valid_transport)):
            valid_transport_str = valid_transport_str + str(valid_transport[i]) + ', '
        valid_transport_str = valid_transport_str[:len(valid_transport_str) - 2]
        print("You can use bus/buses " + valid_transport_str + " to get from " + self.origin + " to " + self.destination)

    #convert python list data into stack
    def create_stack(self):
        for i in range (len(bus_str)):
            bus_str_Stack_temp[i] = Stack()
            for j in range (len(bus_str[i])):
                bus_str_Stack_temp[i].AddElem(bus_str[i][j])
        bus_str_Stack = Stack()
        for i in range (len(bus_str_Stack_temp)):
            bus_str_Stack.AddElem(bus_str_Stack_temp[i])
        return bus_str_Stack