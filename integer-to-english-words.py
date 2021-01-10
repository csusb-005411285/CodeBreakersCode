class Solution:
    def __init__(self):
        self.units =  { 1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', 6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine'}
        self.tens_l20 =  {10: 'Ten', 11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen', 15: 'Fifteen', 16: 'Sixteen', 17: 'Seventeen', 18: 'Eighteen', 19: 'Nineteen' }
        self.tens_g20= { 2: 'Twenty', 3: 'Thirty', 4: 'Forty', 5: 'Fifty', 6: 'Sixty', 7: 'Seventy', 8: 'Eighty', 9: 'Ninety'} 
    
    def numberToWords(self, num: int) -> str:
        if num == 0: 
            return 'Zero'
        english_word = ''
        billion, millionth = divmod(num, 1000000000)
        million, thousandth = divmod(millionth, 1000000)
        thousand, hundred = divmod(thousandth, 1000)
        
        if billion:
            english_word += self.two_digits_to_words(billion) + ' Billion'
        if million:
            english_word += ' ' + self.three_digits_to_words(million) + ' Million' if billion else self.three_digits_to_words(million) + ' Million'
        if thousand:
            english_word += ' ' + self.three_digits_to_words(thousand) + ' Thousand' if billion or million else self.three_digits_to_words(thousand) + ' Thousand'
        if hundred:
            english_word += ' ' + self.three_digits_to_words(hundred) if billion or million or thousand else self.three_digits_to_words(hundred)
        return english_word
    
    def three_digits_to_words(self, num):
        words = ''
        hundred, other = divmod(num, 100)
        if hundred and other: 
            words += self.units[hundred] + ' Hundred ' + self.two_digits_to_words(other)
        elif hundred and other == 0:
            words += self.units[hundred] + ' Hundred'
        elif hundred == 0 and other:
            words += self.two_digits_to_words(other)
        return words
    
    def two_digits_to_words(self, num):
        word = ''
        tens, units = divmod(num, 10)
        if num < 10:
            word += self.units[num]
        elif num < 20:
            word += self.tens_l20[num]
        else:
            if tens and units == 0:
                word += self.tens_g20[tens]
            elif tens and units:
                word += self.tens_g20[tens] + ' ' + self.units[units]
            elif tens == 0 and units:
                word += self.units[units]
        return word
    
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
