# concise
class Solution:
    def __init__(self):
        self.units = {0: '', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten'}
        self.teens = {11: 'eleven', 12:'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen'}
        self.tens = {2: 'twenty', 3: 'thirty', 4: 'forty', 5: 'fifty', 6: 'sixty', 7: 'seventy', 8: 'eighty', 9: 'ninety'}

    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"
        words = ''
        billionth, million = divmod(num, 1000000000)
        millionth, thousand = divmod(million, 1000000)
        thousandth, hundred = divmod(thousand, 1000)
        if billionth:
            words += self.process_three_digits(billionth) + ' Billion'
        if millionth:
            words +=  ' ' + self.process_three_digits(millionth) + ' Million' if billionth else self.process_three_digits(millionth)  + ' Million'
        if thousandth:
            words += ' ' + self.process_three_digits(thousandth) + ' Thousand' if millionth else self.process_three_digits(thousandth) + ' Thousand'
        if hundred:
            words += ' ' + self.process_three_digits(hundred) if thousandth or millionth or billionth else self.process_three_digits(hundred)
        return words
    
    def process_three_digits(self, digits):
        three_digits = ''
        hundredth, tens = divmod(digits, 100)
        # 100, 101, 123, 23, 3, 
        if hundredth:
            three_digits += self.units[hundredth] + ' Hundred'
        if tens:
            three_digits += ' ' + self.process_two_digits(tens) if hundredth else self.process_two_digits(tens)
        return three_digits.title()

    def process_two_digits(self, digits):
        two_digits = ''
        if digits <= 10:
            return self.units[digits]
        if digits < 20:
            return self.teens[digits]
        div, mod = divmod(digits, 10)
        two_digits += self.tens[div] + ' ' + self.units[mod] if self.units[mod] else self.tens[div]
        return two_digits.title()

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
