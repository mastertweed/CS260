class Solution:
    def reverse(self, x):
        nums = [char for char in "1234567890"]

        s1 = [char for char in str(x)]
        s2 = ""
        for i in range(len(s1)):
            if s1[i] not in nums:
                s2 = s1[i]
                s1[i] = ""
        s1.reverse()

        if s2 != "":
            s1.insert(0, s2)

        s2 = "".join(s1)

        if len(s2) != 1:
            s2 = [char for char in s2]

            nums.remove("0")
            for i in range(len(s2)):
                if s2[i] == "0":
                    s2[i] = ""
                elif s2[i] in nums:
                    break

        sOut = int("".join(s2))

        if sOut < 2147483646 and sOut > -2147483647:
            return sOut
        else:
            return 0