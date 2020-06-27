# https://leetcode.com/problems/expressive-words/discuss/121706/Java-Solution-using-Two-Pointers-with-Detailed-Explanation
class Solution:
    def expressiveWords(self, S: str, words: [str]) -> int:
        if not S or not words:
            return 0

        count = 0
        s_map = self.get_map(S)

        for word in words:

            w_map = self.get_map(word)
            if len(w_map.keys()) != len(s_map.keys()):
               continue 

            if self.check_word_is_expressive(S, word):
                count += 1

        return count 
    
    def get_map(self, word):
        c_map = {}

        for char in word:
            if char not in c_map:
                c_map[char] = 1
            else:
                c_map[char] += 1
        
        return c_map
    
    def check_word_is_expressive(self, s, w):
        i = 0
        j = 0

        while i < len(s) and j < len(w):
            if s[i] != w[j]:
                return False
            
            len_s = self.get_num_repeated_chars(s, i)
            len_w = self.get_num_repeated_chars(w, j) 

            if len_w > len_s:
                return False

            if len_s != len_w:
                if len_s < 3:
                    return False
                
                
            i = i + len_s 
            j = j + len_w 
    
        return True
    
    def get_num_repeated_chars(self, s, index):
        num = 1

        while index < len(s) - 1: 
            if s[index] == s[index + 1]: 
                num += 1 
            else:
                break
            
            index += 1
        
        return num 
        
