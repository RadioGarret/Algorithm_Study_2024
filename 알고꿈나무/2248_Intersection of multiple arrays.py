class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        counts = defaultdict(int)
        for array in nums:
            for x in array:
                counts[x] += 1


        n =len(nums)
        answer = []
        for key in counts:
            if counts[key] == n:
                answer.append(key)

        return sorted(answer)