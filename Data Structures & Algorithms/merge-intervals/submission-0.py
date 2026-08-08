class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        #Given an array of intervals where intervals[i] = [start_i, end_i],
        # merge all overlapping intervals, and return an array of the non-overlapping intervals 
        # that cover all the intervals in the input.
        
        intervals = sorted(intervals)
        res = []

        l, r = intervals[0][0], intervals[0][1]
        for _ in range(len(intervals)):
            if intervals[_][0] > r:
                res += [[l,r]]
                l, r = intervals[_][0], intervals[_][1]
                print(l,r)
            if intervals[_][0] < l:
                l = intervals[_][0]
            if intervals[_][1] > r:
                r = intervals[_][1]
        print(res)
        res += [[l,r]]
        return res