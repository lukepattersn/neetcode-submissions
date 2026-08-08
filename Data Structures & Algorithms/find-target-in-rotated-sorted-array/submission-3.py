class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        
        while l <= r:
            mid = (l + r) // 2
            
            if nums[l] <= nums[mid]: # left half sorted
                if nums[l] <= target < nums[mid]:
                # target in nums[l] & nums[mid]
                    r = mid - 1
                else: # target not in sorted left half
                    l = mid + 1 # search right

            else: # right half sorted
                if nums[mid] < target <= nums[r]:
                # target is in the sorted right side
                    l = mid + 1 # search right
                else:
                # target not in sorted right side, must be in left side
                    r = mid - 1 # search left 

            if nums[mid] == target:
                return mid
        else:
            return -1


