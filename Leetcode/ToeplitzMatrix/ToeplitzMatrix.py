class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        for i in range(0,len(matrix)-1):
            if matrix[i][0:len(matrix[i])-1] != matrix[i+1][1:len(matrix[i])]:
                return False
        return True

