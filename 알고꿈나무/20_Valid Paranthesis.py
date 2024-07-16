class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        matching = {"(" : ")" , "[" : "]", "{" : "}"}

        for element in s:
            if element in matching:
                stack.append(element)
            else:
                if not stack:
                    return False

                
                previous_opening = stack.pop()
                if matching[previous_opening] != element:
                    return False 
        return not stack