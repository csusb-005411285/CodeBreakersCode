# tc: o(1), sc: o(1)
    def intToRoman(self, num: int) -> str:
        thousands = ['', 'M', 'MM', 'MMM']
        hundreds = ['', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM']
        tens = ['', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC']
        units = ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX']
        roman = ''

        quotient_thousands = num//1000
        remainder_thoudsands = num%1000
        roman += thousands[quotient_thousands]
        
        quotient_hundreds = remainder_thoudsands//100
        remainder_hundreds = remainder_thoudsands%100
        roman += hundreds[quotient_hundreds] 
        
        quotient_tens = remainder_hundreds//10
        remainder_tens = remainder_hundreds%10
        
        roman += tens[quotient_tens]
        roman += units[remainder_tens]

        return roman
