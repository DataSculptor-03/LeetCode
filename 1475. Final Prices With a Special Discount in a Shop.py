class Solution(object):
    def finalPrices(self, prices):
        """
        :type prices: List[int]
        :rtype: List[int]
        """
        index = 0
        l = []
        for i in range(0, len(prices)):        
            for j in range(i+1, len(prices)):
                if(prices[i] >= prices[j]):
                    cal = prices[i] - prices[j]
                    l.append(cal)
                    index += 1
                    break
            else:
                l.append(prices[i])
        return l
