class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        min = 0

        while l < r:
            mid = (l + r) // 2

            if nums[mid] > nums[r]:
                # pivot right of mid
                l = mid + 1
            else:
                #mid or left of mid in min
                r = mid
        return nums[l]


            