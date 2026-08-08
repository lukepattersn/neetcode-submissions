class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in hashMap.keys():
                return[hashMap[diff], i]          
            hashMap[n] = i