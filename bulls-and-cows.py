class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        # init vars
        # secret_map 
        secret_map = Counter(secret)
        # count bulls
        bulls = 0
        # guess_set
        guess_map = Counter(guess)
        cows = 0
        # inital checks
        
        # process
        # loop through both the strings simultaneously
        for s, g in zip(secret, guess):
            # if chars are equal
            if s == g:
                # increment bulls
                bulls += 1
                # decrement count from both hash maps
                secret_map[s] -= 1
                guess_map[g] -= 1
        # loop through both the dictionaries
        for key, val in secret_map.items():
            if key in guess_map:
                # get the min. value
                # increment cows
                cows += min(secret_map[key], guess_map[key])
        # return
        # count of bulls A + count of elements in set B
        return "{}A{}B".format(bulls, cows)
