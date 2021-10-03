class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        # init vars
        num_subseq = 0
        sptr, tptr = 0, 0
        # initial checks

        # process
        # loop through target
        while tptr < len(target):
            # set vars
            sptr = 0
            # set a flag to indicate char found in source
            char_found = False
            # loop through source
            # we are trying to match the target character
            while sptr < len(source) and tptr < len(target):
                # if chars are equal
                if target[tptr] == source[sptr]:
                    # move both the pointers ahead
                    tptr += 1
                    char_found = True
                # if not
                # move the source pointer ahead
                sptr += 1
            # if flag is set return -1
            if not char_found:
                return -1
            # incr count of num_subsequnces
            num_subseq += 1
        # return
        return num_subseq
