'''
153. Find Minimum in Rotated Sorted Array

Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:

[4,5,6,7,0,1,2] if it was rotated 4 times.
[0,1,2,4,5,6,7] if it was rotated 7 times.

Given the sorted rotated array nums of unique elements, return the minimum element of this array.

You must write an algorithm that runs in O(log n) time.
--------------------------
Example 1:
Input: nums = [3,4,5,1,2]
Output: 1
Explanation: The original array was [1,2,3,4,5] rotated 3 times.
----------------------------
Example 2:
Input: nums = [4,5,6,7,0,1,2]
Output: 0
Explanation: The original array was [0,1,2,4,5,6,7] and it was rotated 4 times.

'''

#---------------------------------

'''
#-------Brute Force Solution-------

class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        res = nums[0]

        for num in nums:
            res = min(num , res)
        return res
test = Solution()
result = test.findMin([4,5,6,7,0,1,2])
print(result)

'''

#-----Solution using Binary Search-----------

class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        res = nums[0]
        l,r = 0, len(nums)-1

        while(l<=r):

            if(nums[l]<nums[r]): #means array is no longer rotated
                return min(res , nums[l])
            
            m = (l+r) // 2
            res = min(nums[m] , res)

            if(nums[l] <= nums[m]):
                l = m+1
            else:
                r=m-1
        return res

test = Solution()
result = test.findMin([4,5,6,7,1,2])
print(result)
