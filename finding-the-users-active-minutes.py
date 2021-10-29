class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        user_map = defaultdict(set) 
        answer = [0] * (k + 1)
        for log in logs: 
            _id, time = log 
            user_map[_id].add(time) 
        for key, val in user_map.items(): 
            uam = len(val) 
            answer[uam] += 1 
        return answer[1:]
