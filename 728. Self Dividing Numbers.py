class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        l = []
        for i in range(left, right + 1): 
            d = i
            count = 0
            temp = i 
            while temp != 0:
                rem = temp % 10
                if rem == 0 or d % rem != 0:
                    break
                count += 1
                temp //= 10
            if count == len(str(d)):
                l.append(d)
        return l
