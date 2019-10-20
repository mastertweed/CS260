class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        for i in range(len(nums2)):
            nums1.append(nums2[i])
            nums1 = sorted(nums1)

        if (len(nums1) % 2) == 0:
            a = (nums1[int((len(nums1) / 2) - 1)] + nums1[int(len(nums1) / 2)]) / 2
        else:
            a = nums1[int((len(nums1) / 2))]

        return a