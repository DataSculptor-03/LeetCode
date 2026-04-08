class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        l=[]
        count=0
        for i in range(0,len(words)):
            if words[i] not in l and words[i][::-1] not in l:
                if words[i][::-1] in words[i+1:]:
                    l.append(words[i])
                    l.append(words[i][::-1])
                    count+=1
        return count
