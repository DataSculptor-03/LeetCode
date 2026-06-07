class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        n = len(nums)

        prev_g = [-1] * n
        next_g = [n] * n
        prev_s = [-1] * n
        next_s = [n] * n

        stack = []
        for i in range(n):
            while stack and nums[stack[-1]] < nums[i]:
                stack.pop()
            prev_g[i] = stack[-1] if stack else -1
            stack.append(i)

        stack = []
        for i in range(n - 1, -1, -1):
            while stack and nums[stack[-1]] <= nums[i]:
                stack.pop()
            next_g[i] = stack[-1] if stack else n
            stack.append(i)

        stack = []
        for i in range(n):
            while stack and nums[stack[-1]] > nums[i]:
                stack.pop()
            prev_s[i] = stack[-1] if stack else -1
            stack.append(i)

        stack = []
        for i in range(n - 1, -1, -1):
            while stack and nums[stack[-1]] >= nums[i]:
                stack.pop()
            next_s[i] = stack[-1] if stack else n
            stack.append(i)

        ans = 0
        for i in range(n):
            max_count = (i - prev_g[i]) * (next_g[i] - i)
            min_count = (i - prev_s[i]) * (next_s[i] - i)
            ans += nums[i] * (max_count - min_count)

        return ans
