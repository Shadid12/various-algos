# https://leetcode.com/problems/generate-parentheses/description/

from typing import List
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
      res = []
      sol = []
      def backtrack(openp, closep):
        # Base case
        if len(sol) == 2 * n:
          res.append(''.join(sol))
          return
        if openp < n:
          sol.append('(')
          backtrack(openp + 1, closep)
          sol.pop()
        
        if closep < openp:
          sol.append(')')
          backtrack(openp, closep + 1)
          sol.pop()
    
      backtrack(0, 0)

      return res        


# Test
l = Solution()
r = l.generateParenthesis(3)
print(r)
# ['(']  # openp = 0, closep = 0
# ['(', '('] # openp = 1, closep = 0
# ['(', '(', '('] # openp = 2, closep = 0