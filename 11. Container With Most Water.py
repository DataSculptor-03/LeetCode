class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        mw=0
        i=0
        j=len(height)-1
        while(i<j):
            cal=j-i
            most=cal*min(height[i],height[j])
            if(mw<most):
                mw=most
            if(height[i]<height[j]):
                i+=1
            else:
                j-=1
        return mw
