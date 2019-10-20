
def maxSubArray(nums):
    if len(nums) == 1: return nums[0]

    if sum(0 for number in nums if number < 0) == 0: return max(nums)

    for i in range(len(nums)):
        for k in range(i, len(nums)):

            a = sum(nums[i:k])

            if a > maxNum:
                maxNum = a

    return maxNum

b = maxSubArray([-2,1,-3,4,-1,2,1,-5,4])
