class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            freq[num] = 1 + freq.get(num, 0)
        sorted_items = sorted(freq.items(), key=lambda x: x[1], reverse=True)
        return [item[0] for item in sorted_items[:k]]