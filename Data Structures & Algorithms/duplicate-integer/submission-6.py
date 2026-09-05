class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        vistos = set()
        for x in nums:
            if x in vistos:
                return True
            else:
                vistos.add(x)
        return False