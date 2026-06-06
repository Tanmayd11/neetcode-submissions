class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        arr =(nums)
        seen = set()
        for num in arr:
            if num in seen:
                return(True)
            seen.add(num)
        return False