import sys
sys.set_int_max_str_digits(0)

from typing import List
class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        s = ''.join(str(d) for d in num)
        total = int(s) + k
        return [int(d) for d in str(total)]
