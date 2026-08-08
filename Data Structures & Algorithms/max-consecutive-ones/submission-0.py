class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        max_count = 0
        for i in nums:
            if i == 1:
                count += 1 
                max_count = max(count, max_count)
            else: # we find a 0
                count = 0

        return max_count