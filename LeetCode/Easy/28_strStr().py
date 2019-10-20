class Solution:
    def strStr(self, haystack, needle):
        if len(haystack) == 0 and len(needle) == 0: return 0
        if haystack == needle: return 0

        if needle not in haystack:
            return -1
        else:
            a = len(haystack)
            b = len(needle)
            for i in range(a - b + 1):
                print(haystack[i:i + b])
                if haystack[i:i + b] == needle:
                    return i
