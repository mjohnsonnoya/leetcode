class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {")" : "(","]" : "[", "}" : "{" }
        for c in s:
            if c in "([{":
                stack.append(c)
            elif c in ")]}":
                if stack and stack[-1] == mapping[c]:
                    stack.pop()
                else:
                    return False
        return not stack

        # pstack = []
        # sstack = []
        # cstack = []
        # for c in s:
        #     if c == "(":
        #         pstack.append(c)
        #     elif c == "[":
        #         sstack.append(c)
        #     elif c == "{":
        #         cstack.append(c)
        #     elif c == ")" and pstack:
        #         pstack.pop()
        #     elif c == "]" and sstack:
        #         sstack.pop()
        #     elif c == "}" and cstack:
        #         cstack.pop()
        #     else:
        #         return False
        # return True

            
        

