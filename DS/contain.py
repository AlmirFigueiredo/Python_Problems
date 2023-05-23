from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums = sorted(nums)
        for i in range(0, len(nums)):
            for j in range(i+1, len(nums)):
                if nums[j] > nums[i]:
                    break
                if nums[j] == nums[i]:
                    return True
        return False
