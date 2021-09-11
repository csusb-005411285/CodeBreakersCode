class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        # init vars
        # a set to store the distances
        distances = set()
        # initial checks
        
        # process
        # get the six distances and add them to a set
        # p1 & p2, p1 & p3, p2 & p4, p3 & p4, p1 & p4, p2 & p3
        '''
        p2  p4
        
        p1  p3
        '''
        distances.add(self.get_distance(p1, p2))
        distances.add(self.get_distance(p1, p3))
        distances.add(self.get_distance(p2, p4))
        distances.add(self.get_distance(p3, p4))
        distances.add(self.get_distance(p1, p4))
        distances.add(self.get_distance(p2, p3))
        # return true is set has only two values
        return len(distances) == 2 and 0 not in distances
    
    def get_distance(self, p1, p2):
        return pow((p1[0] - p2[0]), 2) + pow((p1[1] - p2[1]), 2)
