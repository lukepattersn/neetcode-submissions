class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        res = 0

        while l < r:
            width = r - l
            currHeight = min(heights[r], heights[l])
            area = width * currHeight

            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1

            if area > res:
                res = area
        return res