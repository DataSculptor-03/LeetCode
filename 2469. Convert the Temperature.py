class Solution(object):
    def convertTemperature(self, celsius):
        """
        :type celsius: float
        :rtype: List[float]
        """
        l=[]
        k=273.15+celsius
        l.append(k)
        cal=((9*celsius)/5)+32
        l.append(cal)
        return l
