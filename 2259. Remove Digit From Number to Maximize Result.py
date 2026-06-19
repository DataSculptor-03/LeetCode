class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        ans=""
        for i in range(len(number)):
            if number[i]==digit:
                candidate=number[:i]+number[i+1:]
                ans=max(ans,candidate)
        return ans
