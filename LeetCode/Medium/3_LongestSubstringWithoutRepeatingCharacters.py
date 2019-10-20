class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 1: return 1

        def stringLen(clip):
            sub = []
            for i in range(len(clip)):
                if clip[i] not in sub:
                    sub.append(clip[i])
                else:
                    return len(sub)

            return len(sub)

        maxLen = 0
        for i in range(len(s)):
            l = stringLen(s[i::])

            if l > maxLen:
                maxLen = l

        return maxLen