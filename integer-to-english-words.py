class Solution:
    def __init__(self):
        self.units =  { 1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', 6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine'}
        self.tens_l20 =  {10: 'Ten', 11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen', 15: 'Fifteen', 16: 'Sixteen', 17: 'Seventeen', 18: 'Eighteen', 19: 'Nineteen' }
        self.tens_g20= { 2: 'Twenty', 3: 'Thirty', 4: 'Forty', 5: 'Fifty', 6: 'Sixty', 7: 'Seventy', 8: 'Eighty', 9: 'Ninety'} 
        
    def numberToWords(self, num: int) -> str:
        if num == 0: return 'Zero'
        billion = num//1000000000
        million = (num % 1000000000) // 1000000
        thousand = (num % 1000000) // 1000
        hundred = num%1000
        tens = (num % 100) // 10

        output = ''
        if billion:
            output = self.units[billion] + ' Billion'
        if million:
            output += ' ' if billion else ''
            output += self.three_digits(million) + ' Million'
        if thousand:
            output += ' ' if million or billion else ''
            output += self.three_digits(thousand) + ' Thousand'
        if hundred:
            output += ' ' if thousand or million or billion else ''
            output += self.three_digits(hundred)
        return output

    def two_digits(self, num):
        if num < 10:
            return self.units[num]
        elif num < 20:
            return self.tens_l20[num]
        else:
            tens, ones = divmod(num, 10)
            if tens and not ones:
                return self.tens_g20[tens]
            elif tens and ones:
                return self.tens_g20[tens] + ' ' + self.units[ones]
        
    def three_digits(self, num):
        hundreds, tens = divmod(num, 100)
        if hundreds and tens:
            return self.units[hundreds] + ' Hundred' + ' ' + self.two_digits(tens)
        elif hundreds and not tens:
            return self.units[hundreds] + ' Hundred'
        elif not hundreds and tens:
            return self.two_digits(tens)
