class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        psum = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
        
        for i in range(m):
            for j in range(n):
                psum[i+1][j+1] = mat[i][j] + psum[i][j+1] + psum[i+1][j] - psum[i][j]
        
        ans = [[0 for _ in range(n)] for _ in range(m)]
        
        for i in range(m):
            for j in range(n):
                r1, c1, r2, c2 = max(i-k, 0), max(j-k, 0), min(i+k+1, m), min(j+k+1, n)
                ans[i][j] = psum[r2][c2] - psum[r2][c1] - psum[r1][c2] + psum[r1][c1]
        
        return ans
