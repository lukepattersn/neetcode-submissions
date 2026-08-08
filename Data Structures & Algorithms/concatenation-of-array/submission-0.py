class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = nums.copy() + nums.copy()
        return ans

