class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if len(s) == numRows: return s

        rows = []
        for i in range(numRows):
            rows.append([])

        str_count = 0
        while True:
            for i in range(numRows):
                if str_count < len(s):
                    rows[i].append(s[str_count])
                    str_count += 1

            for i in reversed(range(1, numRows - 1)):
                if str_count < len(s):
                    rows[i].append(s[str_count])
                    str_count += 1

            if str_count == len(s):
                break

        output = ""
        for i in range(len(rows)):
            for k in range(len(rows[i])):
                output = output + str(rows[i][k])

        return output
