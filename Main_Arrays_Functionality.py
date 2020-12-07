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
    def search_street(self, origin, destination):
        valid_transport = []
        valid_indexs = []
        for i in range(len(bus_str)):
            found_locations = []
            valid = 0
            for j in range(len(bus_str[i])):
                if str(bus_str[i][j]) == str(origin) or str(bus_str[i][j]) == str(destination):
                    valid = valid + 1
                    found_locations.append(j)
            if valid == 2:
                valid_transport.append(i)
                valid_indexs.append(found_locations)
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