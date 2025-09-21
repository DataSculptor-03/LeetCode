class Solution(object):
    def finalValueAfterOperations(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        d={"--":-1,"++":1}
        t=0
        for i in operations:
            if i=="--X" or i=="X--":
                t+=-1
            elif i=="X++" or "++X":
                t+=1
        return t
