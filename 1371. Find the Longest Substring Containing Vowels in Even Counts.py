class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        vowel_mask = {'a': 1, 'e': 2, 'i': 4, 'o': 8, 'u': 16}
        seen = {0: -1}
        mask = 0
        max_len = 0
        for i, ch in enumerate(s):
            if ch in vowel_mask:
                mask ^= vowel_mask[ch]
            if mask in seen:
                max_len = max(max_len, i - seen[mask])
            else:
                seen[mask] = i
        return max_len
