class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()
        while True:
            if n == 1:
                return True
            
            if n in visited:
                return False
            
            visited.add(n)

            nums = collections.deque()
            while n != 0:
                nums.append(n % 10)
                n = n // 10
            
            while nums:
                digit = nums.pop()**2
                n += digit
            


