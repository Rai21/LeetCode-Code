from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)

        if n<=2:
            return n

        start = 1
        for i in range(2,n):
            # unique element
            if nums[i]!=nums[start-1]:
                start+=1
                nums[start] = nums[i]
        
        return start+1