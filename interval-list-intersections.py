class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        i = 0 
        j = 0
        if not firstList or not secondList:
            return []
        result = []
        while i < len(firstList) and j < len(secondList):
            intersect = []
            startTime = max(firstList[i][0], secondList[j][0])
            endTime = min(firstList[i][1], secondList[j][1])
            if not endTime < startTime:
                intersect.append(startTime)
                intersect.append(endTime)
                result.append(intersect)
            if firstList[i][1] > secondList[j][1]:
                j += 1
            else:
                i += 1
        return result
    
class Solution:
    def intervalIntersection(self, A: [[int]], B:[[int]]) -> [[int]]:
        res = []
        a = A
        b = B
        i = 0
        j = 0
        while i < len(a) and j < len(b):
            ia = a[i]
            ib = b[j]
            a_intersects_b = False
            b_intersects_a = False
            # at this point the intervals intersect
            # check if a intersects b, or b intersects a, or a and b overlap
            if a[i][0] >= b[j][0] and a[i][0] <= b[j][1]:
                a_intersects_b = True
            elif b[j][0] >= a[i][0] and b[j][0] <= a[i][1]:
                b_intersects_a = True
            # find the start and end times of the intersection
            # add it to the results list  
            if a_intersects_b or b_intersects_a:
                res.append([max(a[i][0], b[j][0]), min(a[i][1], b[j][1])])
            # increment the pointer that points to the interval with a smaller end time
            # why skip smaller end time, and not other options
            # check if the two intervals do not overlap
            if a[i][1] > b[j][0] or b[j][1] > a[i][0]:
                if a[i][1] < b[j][1]:
                    i += 1
                else:
                    j += 1
        # return the results list
        return res
