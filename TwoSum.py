def twoSum(nums, target):
    dict = {}

    for i,val in enumerate(nums):
        n = target - val
        if n not in dict:
            dict[val] = i
        else:
            return [dict[n], i]


nums = [2,7,11,15]
target = 17
twoSum(nums,target)