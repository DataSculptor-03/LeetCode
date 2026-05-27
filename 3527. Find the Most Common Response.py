from collections import Counter

class Solution:
    def findCommonResponse(self, responses: List[List[str]]) -> str:
        group_freq = Counter()

        for group in responses:
            unique_items = set(group)      # prevent double-counting in same group
            for item in unique_items:
                group_freq[item] += 1

        max_groups = max(group_freq.values())
        candidates = [k for k, v in group_freq.items() if v == max_groups]

        return min(candidates)
