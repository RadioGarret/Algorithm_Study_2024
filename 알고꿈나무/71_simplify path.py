class Solution:
    def simplifyPath(self, path: str) -> str:
        
        stack = []
        
        for string in path.split("/"):
            if string in ("","."):
                continue
            if string == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(string)

        return "/" +"/".join(stack)