class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        res = 1
        a %= 1337
        for digit in b:
            res = pow(res, 10, 1337) * pow(a, digit, 1337) % 1337
        return res
