# i started with this code
def threeSumClosest(nums,target):
    min_num = float('inf')
    closest_num = 0
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            for y in range(j+1, len(nums)):
                total = nums[i] + nums[j] + nums[y]
                if(abs(total - target) < min_num):
                    min_num = abs(total_target)
                    closest_num = total
    return closest_num
    
# i optimized and came up with this
def threeSumClosest(nums,target):
    min_num = float('inf')
    closest_num = 0
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if((j+1) < len(nums)):
                total = nums[i] + nums[j] + nums[y]
                if(abs(total - target) < min_num):
                    min_num = abs(total - target)
                    closest_num = total
    return closest_num
                
