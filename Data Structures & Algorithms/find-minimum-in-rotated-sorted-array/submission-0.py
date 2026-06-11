class Solution:
    def findMin(self, nums: List[int]) -> int:
        nums.sort()
        for num in nums:
            return nums[0]