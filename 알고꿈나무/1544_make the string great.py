class Solution:
    def makeGood(self, s: str) -> str:
        stack = []

        for char in s:
            if stack and stack[-1].swapcase() == char:
                # if the last element that went into the stack is equal to the character thats coming in, and if stack is not empty
                stack.pop()

            else:
                stack.append(char)
        
        return ''.join(stack)
