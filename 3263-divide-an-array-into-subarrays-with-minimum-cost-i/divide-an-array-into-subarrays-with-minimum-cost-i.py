class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        if nums.__len__() == 3:
            return sum(nums)
        result = 0
        new_nums = nums[1:]

        first_slice = min(new_nums)
        new_nums.remove(first_slice)
        return nums[0] + first_slice + min(new_nums)