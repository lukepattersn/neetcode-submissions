class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        rightMax = -1
        for i in range(len(arr) -1, -1, -1): # range(start, stop, step)
            newMax = max(rightMax, arr[i]) # save new max BEFORE overwriting
            arr[i] = rightMax # always overwrite with old rightMax
            rightMax = newMax # now update rightMax
                
        return arr
