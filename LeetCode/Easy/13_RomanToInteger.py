class Solution:
    def romanToInt(self, s: str) -> int:
        if len(s) == 0: return 0

        d = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        s = [d[char] for char in s]

        output = 0
        for i in range(len(s)):
            if i < len(s) - 1:
                if s[i] >= s[i + 1]:
                    output += s[i]
                else:
                    output -= s[i]
            else:
                output += s[i]

        return output


