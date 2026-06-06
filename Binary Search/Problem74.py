'''

You are given an m x n integer matrix matrix with the following two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.

 

Example 1:


Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true


'''

#------BruteForce Solution------

'''

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        for row in matrix:
            if(self.searchBin(row, target)):
                return True
        return False
    
    def searchBin(self,row, target):

        l,r=0,len(row)-1
        
        
        while(l<=r):
            m = (l+r) // 2
            if(m == target):

                return True
            elif(target > m):
                l=m+1
            else:  
                r=m-1
        return False

        

test = Solution()
result = test.searchMatrix([[1]], 0)
print(result)

'''

#------Solution using binary search------

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        #Eliminate the rows which are greater and smaller than target value

        row , col = len(matrix) , len(matrix[0])
        top , bot = 0 , row-1

        while(top<=bot): #log(m)
            mrow = (top+bot)//2 #Consider top,bot,mrow as l,r and m respectively as they are named differently

            if(target > matrix[mrow][-1]): #Last element of middle row
                top = mrow + 1
            elif(target < matrix[mrow][0]):
                bot = mrow-1
            else:
                break #We know the target lie in middle row
        if not (top <= bot):
            return False

        row = (top+bot) // 2 #Middle Row after elimination
        l,r = 0, col-1

        while(l<=r): #log(n)
            m=(l+r)//2 #Mid element if mid row
            if(target == matrix[row][m]):
                return True
            elif(target > matrix[row][m]):
                l = m+1
            else:
                r = m-1
        return False

#log(m) + log(n) = log(m*n)

test = Solution()
result = test.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 11)
print(result)
