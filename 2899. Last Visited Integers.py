class Solution:
    def lastVisitedIntegers(self, nums: List[int]) -> List[int]:
        count=0
        seen=[]
        ans=[]
        k=-1
        for i in range(0,len(nums)):
            if nums[i]>=0:
                seen.insert(0,nums[i])
                k=-1
            elif nums[i]<0:
                k+=1
                if k<len(seen):
                    ans.append(seen[k])
                else:
                    ans.append(-1)
        return ans
