# coding=utf-8

class Solution(object):
    def PredictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        import numpy as np 
        l = len(nums)
        dp = np.zeros(shape=(l, l))
        for i in range(l):
            row = 0
            col = i
            while row < l and col < l:
                if row == col:
                    dp[row][col] = nums[row]
                else:
                    dp[row][col] = max(nums[col]-dp[row][col-1],
                                       nums[row]-dp[row+1][col])
                row += 1
                col += 1
        if dp[0][l-1] < 0:
            return False
        return True
                
