class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for x in range(len(nums)):
            find = target - nums[x]
            for y in range(x+1, len(nums)):
                if nums[y] == find:
                    return [x,y]