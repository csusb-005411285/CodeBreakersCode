class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        quotient = 0
        double_dividend = []
        no_steps = []
        negatives = 2
        steps = 1
        if dividend == -2147483648 and divisor == -1:
            return 2147483647
        if dividend > 0:
            negatives -= 1
            dividend = -dividend
        if divisor > 0:
            negatives -= 1
            divisor = -divisor
        while divisor >= dividend:
            double_dividend.append(divisor)
            no_steps.append(steps)
            divisor += divisor
            steps += steps
        for i in reversed(range(len(double_dividend))):
            if double_dividend[i] >= dividend:
                quotient += no_steps[i]
                dividend -= double_dividend[i]
        return quotient if negatives != 1 else -quotient
