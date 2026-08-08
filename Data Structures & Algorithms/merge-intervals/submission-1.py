class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        #Given an array of intervals where intervals[i] = [start_i, end_i],
        # merge all overlapping intervals, and return an array of the non-overlapping intervals 
        # that cover all the intervals in the input.
        
        intervals.sort()
        res = []

        l, r = intervals[0]
        for i in range(1, len(intervals)):
            start, end = intervals[i]
            if start > r:
                res.append([l, r])
                l, r = start, end
            else:
                r = max(r, end)

        res.append([l, r])
        return res