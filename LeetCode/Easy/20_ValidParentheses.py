class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 0: return True
        if (len(s) % 2) != 0: return False

        db = {")": "1", "]": "2", "}": "3"}
        da = {"(": "1", "[": "2", "{": "3"}

        s = [char for char in s]

        c = []
        for i in range(len(s)):

            if s[i] in da:
                c.append(da[s[i]])

            elif s[i] in db:
                if len(c) == 0:
                    return False
                elif db[s[i]] == c[-1]:
                    c.pop(-1)
                else:
                    return False

        if len(c) == 0:
            return True
        else:
            return False
