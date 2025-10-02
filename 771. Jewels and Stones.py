class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        count=0
        for i in range(0,len(jewels)):
            if jewels[i] in stones:
                count=count+stones.count(jewels[i])
        return count
