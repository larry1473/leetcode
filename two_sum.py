from typing import List

def two_sum(nums: List[int], target:int) -> List[int]:
    seen = {}
    for i,num in enumerate(nums):
        if num in seen:
            return [seen[num],i]
        else:
            seen[target - num] = i
    return i