class Solution(object):
    def findArray(self, pref):
        """
        :type pref: List[int]
        :rtype: List[int]
        """
        l = [pref[0]]
        for i in range(1, len(pref)):
            l.append(pref[i] ^ pref[i - 1])
        return l
