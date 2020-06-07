# tc: o(1), sc: o(1)
class Solution:
    def intToRoman(self, num: int) -> str:
        thousands = ['', 'M', 'MM', 'MMM']
        hundreds = ['', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM']
        tens = ['', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC']
        ones = ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX']

        first_digit = num//1000
        second_digit = (num%1000)//100
        third_digit = (num%100)//10
        fourth_digit = num%10

        roman = thousands[first_digit] + hundreds[second_digit] + tens[third_digit] + ones[fourth_digit]
        return roman.strip()
