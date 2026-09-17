class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        total = 0
        zeros = 0
        prod = 1
        res = [0] * n
        for i in range(n):
            if nums[i] == 0:
                zeros += 1
            else:
                prod *= nums[i]
        for i in range(n):
            if zeros > 1:
                return [0 for _ in range(n)]
            elif zeros == 1:
                if nums[i] == 0:
                    res[i] = prod
                else:
                    res[i] = 0
            else:
                res[i] = prod // nums[i]
        return res


        