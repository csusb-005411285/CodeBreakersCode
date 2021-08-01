class Solution:
    def visiblePoints(self, points: List[List[int]], angle: int, location: List[int]) -> int:
        left = 0
        angles = []
        count = 0
        duplicates = 0
        if angle == 360:
            return len(points)
        for point in points:
            x1, y1 = point
            x2, y2 = location
            if x1 == x2 and y1 == y2:
                duplicates += 1
                continue
            angles.append(math.atan2((y2 - y1), (x2 - x1)))
        angles.sort()
        for i in range(len(angles)):
            angles.append(angles[i] + 2 * math.pi)
        d_angles = list(map(lambda x: degrees(x), angles))
        angle = math.pi * angle/180
        for right, val in enumerate(angles):
            while val - angles[left] > angle and left <= right:
                left += 1
            count = max(count, right - left + 1)
        return count + duplicates
