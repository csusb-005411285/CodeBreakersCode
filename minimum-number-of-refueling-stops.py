class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        # init vars
        # max heap
        heap = []
        # count of stops
        stops = 0
        gas_in_tank = startFuel
        prev_pos = 0
        stations.append((target, sys.maxsize)) # 1.
        # inital checks
        
        # process
        # loop through stations
        for pos, gas in stations:
            # check if we have gas in the tank to reach the station
            gas_in_tank -= pos - prev_pos # 2.
            while heap and gas_in_tank < 0:
                # if we do not
                # get the first element from heap
                gas_in_station = heappop(heap)
                # add the gas to the tank
                gas_in_tank += -gas_in_station
                # increment stops
                stops += 1
            if gas_in_tank < 0:
                return -1
            heappush(heap, -gas) # 3.
            prev_pos = pos
        # return number of stops
        return stops

'''
1. add the target to the list of stations
2. the distance is relative. We need to find the distance from the previous station
3. Add the station to the heap in all cases
'''
