def fun(nums,key,index):
    if index<0:
        return 0
    else:
        if nums[index]==key:
            return (1 + fun(nums,key,index-1))
        else:
            return (fun(nums,key,index-1))

nums = [1,5,1]
key = 1
var=fun(nums,key,len(nums)-1)

print(var)

