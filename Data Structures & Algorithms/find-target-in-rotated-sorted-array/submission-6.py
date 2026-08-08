class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2  # compute midpoint

            if target == nums[mid]:
                return mid

            # left sorted portion
            if nums[mid] >= nums[l]:  # equivalent to nums[l] <= nums[mid]
                # Check if target is within the sorted left portion
                if nums[l] <= target <= nums[mid]:
                    r = mid - 1  # search left
                else:
                    l = mid + 1  # search right
                    
            # right sorted portion
            else:
                # Check if target is within the sorted right portion
                if nums[mid] <= target <= nums[r]:
                    l = mid + 1  # search right
                else:
                    r = mid - 1  # search left

        return -1