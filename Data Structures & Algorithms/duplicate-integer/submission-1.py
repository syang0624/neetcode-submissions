class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        unique = set()
        for a in nums:
            if a in unique:
                return True
            unique.add(a)
        return False