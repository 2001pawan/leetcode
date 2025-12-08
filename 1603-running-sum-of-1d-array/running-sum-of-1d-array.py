class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        result= []
        currentsum= 0

        for num in nums:
            currentsum+=num
            result.append(currentsum)

        return result