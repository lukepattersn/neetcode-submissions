class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        seen = {}

        for num in nums:
            seen[num] = 1 + seen.get(num, 0)

        for num, count in seen.items():
            if count == 1:
                return num