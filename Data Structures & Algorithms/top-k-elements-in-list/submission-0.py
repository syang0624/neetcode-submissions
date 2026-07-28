class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashMap = defaultdict(int)
        for num in nums:
            hashMap[num] += 1
        
        sorted_items = sorted(hashMap.items(), key=lambda x: x[1], reverse=True)
        return [key for key, value in sorted_items[:k]]