class Solution:
    def __init__(self):
        self.all_possible = []
        
    def addOperators(self, num: str, target: int) -> List[str]:
        self._add_operators(0, 0, 0, 0, [], target, num)
        return self.all_possible
        
    def _add_operators(self, index, prev, curr, value, curr_comb, target, num):
        #base case
        if index == len(num):
            if value == target and curr == 0:
                self.all_possible.append(''.join(curr_comb[1:]))
            return
        
        # get curr
        curr = (curr * 10) + int(num[index])
        
        # no op
        if curr > 0:
            self._add_operators(index + 1, prev, curr, value, curr_comb, target, num)
        # check for leading 0

        # add
        curr_comb.append('+')
        curr_comb.append(str(curr))
        self._add_operators(index + 1, curr, 0, value + curr, curr_comb, target, num)
        curr_comb.pop()
        curr_comb.pop()

        # sub
        if curr_comb:
            curr_comb.append('-')
            curr_comb.append(str(curr))
            self._add_operators(index + 1, -curr, 0, value - curr, curr_comb, target, num)
            curr_comb.pop()
            curr_comb.pop()

        # mult
            curr_comb.append('*')
            curr_comb.append(str(curr))
            self._add_operators(index + 1, curr * prev, 0, value - prev + (curr * prev), curr_comb, target, num)
            curr_comb.pop()
            curr_comb.pop()
        return
        
