class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        seen = {}

        for i, num in enumerate(numbers):
            compliment = target - num
            if compliment in seen:
                return [seen[compliment] + 1, i + 1]
            seen[num] = i