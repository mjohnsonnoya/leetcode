class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        ans = 0
        place = 1
        mapping = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
        for i in reversed(range(len(num2))):
            k = 1
            for j in reversed(range(len(num1))):
                ans += (mapping[num2[i]] * place) * (mapping[num1[j]] * k)
                k *= 10
            place *= 10
        
        return str(ans)




        
