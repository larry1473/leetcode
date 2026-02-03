def fourSum(nums,target):
    nums.sort()
    n = len(nums)
    res = set()
    for i in range(n):
        for j in range (i+1, n-2):
            new_target = target - (nums[i] + nums[j])
            seen = {}
            new_nums = nums[j+1:]
            for k, num in enumerate(new_nums):
                if num in seen:
                    res.add((nums[i],nums[j],new_nums[seen[num]],num))
                else:
                    seen[new_target - num] = k
             
    return [list(t) for t in res]
        