class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums) + 1
        # xorr = n
        # for i in range(n):
        #     xorr ^= i ^ nums[i]
        
        # return xorr

        nums_sum = 0

        for i in range(0, n):
            nums_sum += i

        return abs(sum(nums) - nums_sum)
            
