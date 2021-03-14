class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        ord_map = defaultdict(list)
        for i, string in enumerate(strings):
            key = self.get_key(string)
            ord_map[key].append(string) 
        return ord_map.values()
    
    def get_key(self, s):
        if len(s) == 1:
            return ','
        keys = []
        for i in range(len(s) - 1): 
            char = s[i] 
            diff = (ord(char) - ord(s[i + 1])) 
            key = diff if diff >= 0 else 26 + diff 
            keys.append(str(key))
        return ','.join(keys)
