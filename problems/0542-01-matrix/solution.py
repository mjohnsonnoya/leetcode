# from queue import Queue
import queue
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat),len(mat[0])
        # maxdist = m*n
        res = [[float('inf') for _ in range(n)] for _ in range(m)]
        graphq = queue.Queue()
        
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    res[i][j] = 0
                    graphq.put((i,j))
                    
        while not graphq.empty():
            i,j = graphq.get()
            if i < m-1 and 1 + res[i][j] < res[i+1][j]:
                res[i+1][j] = 1 + res[i][j]
                graphq.put((i+1,j))
            if i > 0 and 1 + res[i][j] < res[i - 1][j]:
                res[i - 1][j] = 1 + res[i][j]
                graphq.put((i - 1, j))
            if j < n - 1 and 1 + res[i][j] < res[i][j + 1]:
                res[i][j + 1] = 1 + res[i][j]
                graphq.put((i, j + 1))
            if j > 0 and 1 + res[i][j] < res[i][j - 1]:
                res[i][j - 1] = 1 + res[i][j]
                graphq.put((i, j - 1))
        return res 
