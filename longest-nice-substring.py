class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        longest_substring = ''
        for i in range(len(s)):
            for j in range(i):
                count = 0
                substr = s[j: i + 1]
                for k in range(len(substr)):
                    if substr[k].isupper():
                        if substr[k].lower() in substr:
                            count += 1
                    elif substr[k].islower():
                        if substr[k].upper() in substr:
                            count += 1
                    if count == len(substr):
                        if len(substr) > len(longest_substring):
                            longest_substring = substr
        return longest_substring
    
