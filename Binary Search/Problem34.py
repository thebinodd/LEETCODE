'''
Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
Example 3:

Input: nums = [], target = 0
Output: [-1,-1]

'''


#------BruteForce Solution------
'''
class Solution(object):
    def searchRange(self, nums, target):

        first = -1
        last = -1

        for i in range(len(nums)):
            if nums[i] == target:
                if first == -1:
                    first = i
                last = i

        return [first, last]
        
        
test = Solution()
result = test.searchRange([] , 0)
print(result)
'''

#------Solution using binary search------

class Solution(object):
    def searchRange(self, nums, target):
        return [self.binSearch(nums, target, True) , self.binSearch(nums , target, False)]


    def binSearch(self, nums, target, isLeftSearch):

        l,r = 0,len(nums)-1
        i=-1

        while(l<=r):
            m = (l+r) // 2

            if(nums[m] > target):
                r = m-1
            elif(nums[m]<target):
                l=m+1
            else:
                i=m
                if(isLeftSearch):  #Find the index of leftmost index of target
                    r=m-1 
                else: #Find the index of Rightmost index of target
                    l=m+1 
        return i

        
        
test = Solution()
result = test.searchRange([5,7,7,8,8,10] , 8)
print(result)