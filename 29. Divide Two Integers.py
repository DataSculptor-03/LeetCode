class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if dividend == -2**31 and divisor == -1:
            return 2**31 - 1  # Handle overflow case

        sign = -1 if (dividend < 0) != (divisor < 0) else 1

        dividend = abs(dividend)
        divisor = abs(divisor)

        result = dividend // divisor

        return sign * result
