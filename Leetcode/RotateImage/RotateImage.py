class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        t = []
        j = 0
        for i in range(0, len(matrix)):
            for j in range(0, len(matrix[i])):
                t.append(matrix[j][i])
        s = [t[i:i+j+1] for i in range(0, len(t), j+1)]
        r = [i[::-1] for i in s[::-1]]
        matrix.clear()
        for i in range(len(r)-1, 0, -1):
            matrix.append(r[i])
        matrix.append(r[i-1])
        return matrix

