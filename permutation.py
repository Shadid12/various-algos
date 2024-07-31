from typing import List

class Solution:
  def permute(self, nums: List[int]) -> List[List[int]]:
    sol = []
    res = []

    def backtrack(i):

      if len(sol) == len(nums):
        res.append(sol.copy())
        return
      for i in range(len(nums)):
        if nums[i] not in sol:
          sol.append(nums[i])
          backtrack(i + 1)
          sol.pop()
    backtrack(0)
    return res

# Test
l = Solution()
r = l.permute([1, 2, 3])
print(r)
