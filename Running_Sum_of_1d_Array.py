from typing import List

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        n = len(nums)

        ans = []
        ans.appens(nums[0])

        for i in range(1, n):
            x = ans[i-1] + nums[i]
            ans.append(x)
        return ans