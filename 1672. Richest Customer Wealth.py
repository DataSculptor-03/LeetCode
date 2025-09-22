class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        l=[]
        for i in range(len(accounts)):
            cal=sum(accounts[i])
            l.append(cal)
        return max(l)
