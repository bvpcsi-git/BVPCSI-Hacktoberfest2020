"""
Given a square matrix mat, return the sum of the matrix diagonals.

Only include the sum of all the elements on the primary diagonal and all the elements on the secondary diagonal that are not part of the primary diagonal.

Given a square matrix mat, return the sum of the matrix diagonals.

Only include the sum of all the elements on the primary diagonal and all the elements on the secondary diagonal that are not part of the primary diagonal.

Input: mat = [[1,2,3],
              [4,5,6],
              [7,8,9]]
Output: 25
Explanation: Diagonals sum: 1 + 5 + 9 + 3 + 7 = 25
Notice that element mat[1][1] = 5 is counted only once.
"""
class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        s=0
        l , mid = len(mat) , len(mat)//2
        for i in range(l):
            s+= mat[i][i]
            s+= mat[l-i-1][i]
        if l%2 == 1:
            s-=mat[mid][mid]
        return s
    
    
    """
            The primary diagonal is formed by the elements A00, A11, A22, A33.
        Condition for Primary Diagonal:
            The row-column condition is row = column.

        The secondary diagonal is formed by the elements A03, A12, A21, A30. 
        Condition for Secondary Diagonal:
            The row-column condition is row = numberOfRows - column -1.
    """
