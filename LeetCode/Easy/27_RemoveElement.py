class Solution:
    def removeElement(self, nums, val) -> int:
        if len(nums) == 0: return 0
        for i in reversed(range(len(nums))):
            if nums[i] == val:
                nums.pop(i)

        return len(nums)
