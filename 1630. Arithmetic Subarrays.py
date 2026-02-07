class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        li = []
        for i in range(len(l)):
            arr = nums[l[i]:r[i] + 1]
            arr.sort()
            diff = arr[1] - arr[0]
            for j in range(0, len(arr) - 1):
                if arr[j+1] - arr[j] != diff:
                    li.append(False)
                    break
            else:
                li.append(True)
        return li
