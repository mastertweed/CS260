class Solution:
    def myAtoi(self, s) -> int:
        if len(s) == 0: return 0

        nums = "0123456789"
        syms = "+-"

        pre = ""
        output = ""

        for i in range(len(s)):
            if s[i] != " ":
                if s[i] not in nums and s[i] not in syms:
                    break
                else:
                    output = output + s[i]
            elif len(output) > 0:
                break

        s = ""
        for i in range(len(output)):
            if output[i] in syms:
                if len(s) > 0:
                    break
                else:
                    pre = pre + output[i]
            else:
                s = s + output[i]

        output = s

        if len(pre) > 1: return 0
        if len(output) == 0: return 0

        output = pre + output

        r = int(output)

        if r < -2 ** 31:
            return -2 ** 31
        elif r > (2 ** 31) - 1:
            return (2 ** 31) - 1
        else:
            return r


