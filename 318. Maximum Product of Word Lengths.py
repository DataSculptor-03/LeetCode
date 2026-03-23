class Solution:
    def maxProduct(self, words: List[str]) -> int:
        max_product = 0
        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                if not (set(words[i]) & set(words[j])):
                    product = len(words[i]) * len(words[j])
                    max_product = max(max_product, product)
        return max_product
