def fourSum(nums, target):
    nums.sort()
    n = len(nums)
    res = set()

    for i in range(n - 3):
        for j in range(i + 1, n - 2):
            new_target = target - (nums[i] + nums[j])
            seen = {}

            for k in range(j + 1, n):
                num = nums[k]
                if num in seen:
                    res.add((nums[i], nums[j], nums[seen[num]], num))
                else:
                    seen[new_target - num] = k

    return [list(t) for t in res]
        