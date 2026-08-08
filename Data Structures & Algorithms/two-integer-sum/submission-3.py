class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevNum = {}
        for i, v in enumerate(nums):
            complement = target - v
            if complement in prevNum:
                j = prevNum[complement]
                return [j, i]
            prevNum[v] = i