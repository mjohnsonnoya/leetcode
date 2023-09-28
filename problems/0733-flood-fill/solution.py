class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if image[sr][sc] == color:
            return image
        m, n = len(image) - 1, len(image[0]) - 1
        oldColor = image[sr][sc]
        def helper(sr,sc,color):
            image[sr][sc] = color
            if sc < n:
                if image[sr][sc + 1] == oldColor:
                    helper(sr,sc+1, color)
            if sc > 0:
                if image[sr][sc - 1] == oldColor:
                    helper(sr,sc-1, color)
            if sr < m:
                if image[sr+1][sc] == oldColor:
                    helper(sr+1,sc, color) 
            if sr > 0:
                if image[sr-1][sc] == oldColor:
                    helper(sr-1,sc, color) 
        helper(sr,sc,color)
        return image
