'''
Created by Areg Karapetyan
'''

from Main_Data import *
from DS_HashMap import *

class BusStreets:
    def __init__(self,origin,destination):
        self.origin = origin
        self.destination = destination

    # Search for the origin and destination
    # Get valid transport which includes both origin and destination
    # Get index of each street in the list
    def search_street_HM(self,origin, destination, bus_str_HM):
        # print(bus_str_HM.get(1).get(0))
        valid_transport = []
        valid_indexs = []
        for i in range (bus_str_HM.size()):
            found_locations = []
            valid = 0
            for j in range(bus_str_HM.get(i).size()):
                if str(bus_str_HM.get(i).get(j)) == str(origin) or str(bus_str_HM.get(i).get(j)) == str(destination):
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

    #convert python list data into hashmap
    def create_hashmap(self):
        for i in range (len(bus_str)):
            bus_str_HM_temp[i] = HashMap(len(bus_str[i]))
            for j in range (len(bus_str[i])):
                bus_str_HM_temp[i].put(j,bus_str[i][j])
        bus_str_HM = HashMap(len(bus_str))
        for i in range (len(bus_str_HM_temp)):
            bus_str_HM.put(i,bus_str_HM_temp[i])
        return bus_str_HM