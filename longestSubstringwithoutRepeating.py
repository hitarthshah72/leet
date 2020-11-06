class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        dict = {}
        maxCurrent= 0 
        for i in range(len(s)):
            if s[i] in dict and start <= dict[s[i]]:
                start = dict[s[i]] + 1
            else:
                maxCurrent = max(maxCurrent, i - start + 1)
            dict[s[i]] = i
        return maxCurrent
            
