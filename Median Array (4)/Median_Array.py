'''
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

Worked on by Dylan Hermosillo & Levi Taylor

Accepted on Leetcode (should be refactored for updating complexity)
'''

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) == 0:
            if len(nums2) % 2 == 0:  # even value
                first_middle = len(nums2) // 2 - 1
                second_middle = len(nums2) // 2

                midval = (nums2[first_middle] + nums2[second_middle]) / 2
            else:
                middle = len(nums2) // 2
                midval = nums2[middle]
            return midval
        if len(nums2) == 0:
            if len(nums1) % 2 == 0:  # even value
                first_middle = len(nums1) // 2 - 1
                second_middle = len(nums1) // 2

                midval = (nums1[first_middle] + nums1[second_middle]) / 2
            else:
                middle = len(nums1) // 2
                midval = nums1[middle]
            return midval

        nums3 = []
        index_l = 0
        index_r = 0

        while len(nums3) < len(nums1) + len(nums2):
            if nums1[index_l] <= nums2[index_r]:
                nums3.append(nums1[index_l])
                index_l += 1
            else:
                nums3.append(nums2[index_r])
                index_r += 1
            if index_r == (len(nums2)):
                nums3 += nums1[index_l:]
                break
            if index_l == (len(nums1)):
                nums3 += nums2[index_r:]
                break
        # Step 3 Determine middle value
        if len(nums3) % 2 == 0:  # even value
            first_middle = len(nums3) // 2 - 1
            second_middle = len(nums3) // 2

            midval = (nums3[first_middle] + nums3[second_middle]) / 2
        else:
            middle = len(nums3) // 2
            midval = nums3[middle]
        # Step 4 return middle value
        return midval