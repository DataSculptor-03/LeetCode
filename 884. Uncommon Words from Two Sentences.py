class Solution(object):
    def uncommonFromSentences(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: List[str]
        """
        words = s1.split() + s2.split()
        freq = {}

        # Count frequencies manually
        for w in words:
            if w in freq:
                freq[w] += 1
            else:
                freq[w] = 1

        # Return words that appear exactly once
        return [w for w in freq if freq[w] == 1]
