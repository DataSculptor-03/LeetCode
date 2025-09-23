class Solution(object):
    def leftRightDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        l=[]
        l1=[0]
        l2=[]
        s1=0
        s2=0
        for i in range(0,len(nums)-1):
            s1+=nums[i]
            l1.append(s1)
        for j in range(len(nums)-1,0,-1):
            s2+=nums[j]
            l2.append(s2)
        l2.append(0)
        l2.sort()
        l2.reverse()

        for i in range(0,len(l1)):
            cal=abs(l1[i]-l2[i])
            l.append(cal)
        return l
        
