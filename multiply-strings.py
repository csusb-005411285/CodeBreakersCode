class Solution:
    # https://leetcode.com/problems/multiply-strings/discuss/357917/Simple-7-line-Python-Solution-ASCII-values
    def multiply(self, num1: str, num2: str) -> str:
        n1, n2 = ord(num1[0]) - ord('0'), ord(num2[0]) - ord('0')

        for i in range(1, len(num1)):
            n1 = (n1 * 10) + ord(num1[i]) - ord('0')

        for j in range(1, len(num2)):
            n2 = (n2 * 10) + ord(num2[j]) - ord('0')
      
        return str(n1 * n2)
