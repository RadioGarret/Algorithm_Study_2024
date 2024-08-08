class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(path, start, curr ):
            if curr == target: #Base case
                answer.append(path[:])
                return

            for i in range(start, len(candidates)):
                num = candidates[i] #Selects the current candidate number
                if curr +num <= target: # Checks if adding this number to the current sum does not exceed the target
                    path.append(num)
                    backtrack(path, i, curr+num) #Recursively calls the backtrack function to explore further with the updated path and sum.
                    path.pop()




        answer = []
        backtrack([], 0 ,0)  #starting index 0 and current sum 0

        return answer
