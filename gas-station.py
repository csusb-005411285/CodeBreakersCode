class Solution:
    def canCompleteCircuit(self, gas: [int], cost: [int]) -> int:
        starting_station = 0
        gas_in_tank = 0
        if sum(gas) - sum(cost) < 0: return -1
        for station, gas_available in enumerate(gas):
            gas_in_tank += gas_available
            if cost[station] > gas_in_tank:
                starting_station = station + 1 
                gas_in_tank = 0
            else:
                gas_in_tank -= cost[station]
        return starting_station 
