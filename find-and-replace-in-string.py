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
