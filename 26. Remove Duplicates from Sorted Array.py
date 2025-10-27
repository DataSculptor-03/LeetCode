class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s = set()
        index = 0  # Where to write next unique value

        for i in nums:
            if i not in s:
                s.add(i)
                nums[index] = i  # Overwrite in nums itself
                index += 1

        return index
