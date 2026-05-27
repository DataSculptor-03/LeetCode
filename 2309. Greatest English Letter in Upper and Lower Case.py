class Solution:
    def greatestLetter(self, s: str) -> str:
        letters = set(s)
        ans = ""

        for ch in letters:
            if ch.isupper() and ch.lower() in letters:
                ans = max(ans, ch)

        return ans
