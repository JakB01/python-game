nums = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
print(nums, "fourth item original")
a = nums[4]
print(nums, "<<fourth item changed")
var = nums [-1]
print(var, "<<var value")
nums.insert(0, a)

nums.sort(reverse=True)

print("List length ->",len(nums))

print(nums)