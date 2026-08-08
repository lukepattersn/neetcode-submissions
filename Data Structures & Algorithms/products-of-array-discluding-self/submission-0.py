class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = nums.copy()
        hashmap = {i: v for i, v in enumerate(nums)}
        
        for i, v in hashmap.items():
            temp = v
            hashmap[i] = 1
            output[i] = math.prod(hashmap.values())
            hashmap[i] = temp
        return output