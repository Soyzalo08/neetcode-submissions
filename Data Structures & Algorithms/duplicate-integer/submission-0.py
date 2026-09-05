class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        vistos = set()
        for x in nums:
            if x not in vistos:
                vistos.add(x)
            else:
                return True

        return False