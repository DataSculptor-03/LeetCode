class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        arr = list(s)
        l, r = 0, len(arr) - 1

        while l < r:
            if arr[l] != arr[r]:
                smaller = min(arr[l], arr[r])
                arr[l] = arr[r] = smaller
            l += 1
            r -= 1
        
        return "".join(arr)
