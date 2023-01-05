def has_dupes(nums):
    nums.sort()
    for i in range (1, len(nums)):
        if nums[i] == nums[i-1]:
            return True;
    return False;


nums = [1,5,1]

print(checkforDuplicates(nums))
