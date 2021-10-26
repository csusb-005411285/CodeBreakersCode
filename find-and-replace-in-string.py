class Solution:
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        # init vars
        replaced_string = []
        index_map = defaultdict(int)
        indices_set = set(indices)
        # initial checks
        
        # process
        # 0 1 2 3
        # a b c d
        # s = "abcd", indices = [0, 2], sources = ["a", "cd"], targets = ["eee", "ffff"]
        for i, val in enumerate(indices): # 1, 2
            index_map[val] = i # {0: 0, 2: 1}
        # abcd  
        i = 0
        while i < len(s): # 2 c
            char = s[i]
            if i in indices_set: # 2
                val = index_map[i] # 1
                substr = sources[val] # 'cd'
                if s[i: i + len(substr)] == substr: # s[2: 4] == cd
                    replaced_string.append(targets[val]) # ['eee', 'b', 'ffff']
                    i += len(substr) # 2 + 2 = 4
                    continue
            replaced_string.append(char)
            i += 1
        # return
        return ''.join(replaced_string)
    
class Solution:
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        # init vars
        string = list(s)
        # inital checks 
        
        # process
        # loop through indices
        for idx, i in enumerate(indices):
            # if substring at index i equals the string in sources
            if s[i: i + len(sources[idx])] == sources[idx]: 
                # for all the indices of the original string, assign it empty space
                for j in range(i, i + len(sources[idx])):
                    string[j] = ''
                # replace the string with its replacement in the targets list
                # assign the replacement string to the index
                string[i] = targets[idx]
        # return
        return ''.join(string)
