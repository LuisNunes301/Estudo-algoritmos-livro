class Solution:
    def search(self, nums: list[int], target: int):
        l, r = 0, len(nums)-1
        while l <= r:
            m = (l+r)//2
            if nums[m] == target:
                return m
            elif nums[m] < target:
                l = m+1
            else:
                r = m-1
        return -1


bs = Solution()
my_list = list(range(100))
print(bs.search(my_list, 5))  # => 0
