class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        l, r = 0, len(matrix[0]) - 1
        top, bottom = 0, len(matrix) - 1

        while l < r and top < bottom:
            cy, cx = top, l
            while cx < r:
                res.append(matrix[cy][cx])
                cx += 1
            while cy < bottom:
                res.append(matrix[cy][cx])
                cy += 1
            while cx > l:
                res.append(matrix[cy][cx])
                cx -= 1
            while cy > top:
                res.append(matrix[cy][cx])
                cy -= 1


            top += 1
            bottom -= 1
            r -= 1
            l += 1
            print("l: ", l)
            print("r: ", r)
            print("top: ", top)
            print("bottom: ", bottom)
        
        while l <= r and top == bottom:
            res.append(matrix[top][l])
            l += 1
        
        while l == r and top <= bottom:
            res.append(matrix[top][l])
            top += 1

        return res
            

