class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        s = {} 
        for i, n in enumerate(nums):
            d = target - nums[i]
            if d in s:
                return [list(s.keys()).index(d), i]
            else:
                s[n] = i
