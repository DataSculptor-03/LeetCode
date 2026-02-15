class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        pairs=0
        non=0
        l=[]
        s=set(nums)
        for i in s:
            c = nums.count(i)
            pairs += c // 2
            non += c % 2        
        return [pairs, non]
