class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        tA=ord(target)
        a=[]
        for i in letters:
            c=ord(i)
            if tA<c:
                a.append(c)
        if not a:
            return letters[0]
        a.sort()
        return chr(a[0])
