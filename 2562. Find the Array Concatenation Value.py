class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        s1=0
        s2=0
        if len(nums)%2!=0:
            i=0
            j=len(nums)-1
            while(i<j):
                c=str(nums[i])+str(nums[j])
                s1+=int(c)
                i+=1
                j-=1 
            s1+=nums[len(nums)//2]   
        else:
            i=0
            j=len(nums)-1
            while(i<=j):
                c=str(nums[i])+str(nums[j])
                s2+=int(c)
                i+=1
                j-=1
        if len(nums)%2!=0:
            return s1
        else:
            return s2
