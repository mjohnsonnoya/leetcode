class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a_len = len(a)
        b_len = len(b)
        i = 0
        carry = 0

        answer = []

        while i < a_len or i < b_len or carry:
            bit1 = int(a[a_len - 1 - i]) if i < a_len else 0
            bit2 = int(b[b_len - 1 - i]) if i < b_len else 0
            total = bit1 + bit2 + carry
            carry = 1 if (total // 2 == 1) else 0
            bit3 = "1" if (total % 2 == 1) else "0"
            answer.append(bit3)
            i += 1
        return "".join(reversed(answer))



