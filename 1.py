class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i, num in enumerate(nums):
            need = target - num
            if need in hashmap:
                return [hashmap[need], i]
            hashmap[num] = i
