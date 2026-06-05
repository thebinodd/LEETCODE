'''

Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4

'''


#------BruteForce Solution------

'''
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        for index,num in enumerate(nums):
            if(num == target):
                return index
        
        return -1

test = Solution()
result = test.search([-1,0,3,5,9,12],9)
print("The Result is", result)

'''

#------Solution using Binary Search------

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left, right = 0 , len(nums)-1

        while(left<=right):
            mid = (left + right)/2
            mid = int(mid)
            if(nums[mid] == target):
                return mid
            elif(nums[mid]<target):
                left = mid +1
            else:
                right = mid-1
        return -1

test = Solution()
result = test.search([-1,0,3,5,9,12],9)
print("The Result is", result)