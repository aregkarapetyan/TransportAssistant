'''
Created by Areg Karapetyan
'''

from Main_Data import *
from DS_Single_Linked_List import *

class BusStreets:
    def __init__(self,origin,destination):
        self.origin = origin
        self.destination = destination

    # Search for the origin and destination
    # Get valid transport which includes both origin and destination
    # Get index of each street in the list
    def search_street_SLL(self,origin,destination,bus_str_LL):
        valid_transport = []
        valid_indexs = []
        bus_str_LL_loop=bus_str_LL
        for i in range(bus_str_LL.Size()):
            bus_id = 0
            while bus_str_LL_loop.HeadVal is not None:
                found_locations = []
                valid = 0
                valid_index = 0
                while bus_str_LL_loop.HeadVal.DataVal.HeadVal is not None:
                    if bus_str_LL_loop.HeadVal.DataVal.HeadVal.DataVal == str(origin) or bus_str_LL_loop.HeadVal.DataVal.HeadVal.DataVal == str(destination):
                        valid = valid + 1
                        found_locations.append(valid_index)
                    valid_index = valid_index + 1
                    bus_str_LL_loop.HeadVal.DataVal.HeadVal=bus_str_LL_loop.HeadVal.DataVal.HeadVal.NextVal
                if valid == 2:
                    valid_transport.append(bus_id)
                    valid_indexs.append(found_locations)
                bus_id = bus_id + 1
                bus_str_LL_loop.HeadVal=bus_str_LL_loop.HeadVal.NextVal
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

    #convert python list data into single linked list
    def create_linked_list(self):
        for i in range (len(bus_str)):
            bus_str_LL_temp[i] = SLinkedList()
            for j in range (len(bus_str[i])):
                bus_str_LL_temp[i].AtEnd(bus_str[i][j])
            #print("---------------")
            #bus_str_LL_temp[i].ListPrint()
        bus_str_LL = SLinkedList()
        for i in range (len(bus_str_LL_temp)):
            bus_str_LL.AtEnd(bus_str_LL_temp[i])
            #print("---------")
        return bus_str_LL