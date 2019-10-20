class Solution:
    def letterCombinations(self, digits: str):
        if len(digits) == 0: return

        d = {'2': ['a', 'b', 'c'],
             '3': ['d', 'e', 'f'],
             '4': ['g', 'h', 'i'],
             '5': ['j', 'k', 'l'],
             '6': ['m', 'n', 'o'],
             '7': ['p', 'q', 'r', 's'],
             '8': ['t', 'u', 'v'],
             '9': ['w', 'x', 'y', 'z']}

        output = d[digits[0]]

        for digit in range(1, len(digits)):
            temp = []

            for i in range(len(output)):
                for k in range(len(d[digits[digit]])):
                    letter = d[digits[digit]][k]

                    temp.append(output[i] + letter)

            output = temp

        return output



