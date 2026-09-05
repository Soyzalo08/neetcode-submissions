class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complemento = {}
        for i, n in enumerate(nums):
            comp = target - n
            if comp  in complemento:
                return [complemento[comp], i]
            complemento[n] = i