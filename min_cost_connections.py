import heapq
from collections import defaultdict


class WeightedConnection:
    
    def __init__(self, con, direction):
        self.con = con
        self.firstTown = con.firstTown
        self.secondTown = con.secondTown
        self.direction = direction
        self.cost = con.cost
        
    def __lt__(self, con):
        return self.cost < con.cost
    
    def __le__(self, con):
        return self.cost <= con.cost
    
    def __eq__(self, con):
        return self.cost == con.cost
    
    def __ge__(self,con):
        return self.cost >= con.cost
    
    def __gt__(self, con):
        return self.cost > con.cost
    
    def set_direction(self, direction):
        self.direction = direction
    
    def get_second_town(self):
        if self.direction == True:
            return self.secondTown
        elif self.direction == False:
            return self.firstTown
        return None
    
    def get_con(self):
        return self.con
    
def minimumCostConnection(num, connection):
    neighbor_wcs = defaultdict(list)
    entire_city = set()
    for con in connection:
        wc_forward = WeightedConnection(con, True)
        wc_backward = WeightedConnection(con, False)
        entire_city.add(con.firstTown)
        entire_city.add(con.secondTown)
        neighbor_wcs[con.firstTown].append(wc_forward)
        neighbor_wcs[con.secondTown].append(wc_backward)
    
    if len(entire_city) == 0:
        return []
    
    heap_pq = list()
    init = connection[0].firstTown
    for wc in neighbor_wcs.get(init):
        heap_pq.append(wc)
    heapq.heapify(heap_pq)
    min_wc_towns = set({init})
    min_wcs = list()
    
    while len(heap_pq) > 0:
        wc = heapq.heappop(heap_pq)
        if wc.get_second_town() not in min_wc_towns:
            min_wcs.append(wc.get_con())
            min_wc_towns.add(wc.get_second_town())
            for new_wc in neighbor_wcs.get(wc.get_second_town()):
                heapq.heappush(heap_pq, new_wc)
    if entire_city != min_wc_towns:
        return []
    return min_wcs
