class Solution:
    def buttonWithLongestTime(self, events: List[List[int]]) -> int:
        m=events[0][1]
        ans=events[0][0]
        for i in range(0,len(events)-1):
            diff = events[i+1][1] - events[i][1]
            btn = events[i+1][0]

            if diff > m or (diff == m and btn < ans):
                m = diff
                ans = btn

        return ans
