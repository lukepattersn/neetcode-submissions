class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # given an array of int nums, return the len of the longest consecutive sequence of 
        # elements that can be formed

        # a consecutive sequence is a sequence of elements in which each element is exactly
        # 1 greater than the previous elements

        # the elements do not have to be consecutive in the original array

        # so basically we are given an array of int nums, and we must return the length of the longest
        # consecutive sequence of elements that can be formed (e.g, 1,2,3,4,5 outputs 5)

        # when i first think about this I'm thinking about what data 
        res = 0
        store = set(nums)

        for num in nums:
            streak, curr = 0, num

            # while our number is in array increment it my 1 and 
            # check again while also incrementing streak
            while curr in store:
                curr += 1
                streak += 1
            res = max(res, streak)
        return res