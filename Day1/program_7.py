def FirstOccurence(nums, element, i):
    if i == len(nums):
        return -1
    if nums[i] == element:
        return i
    return FirstOccurence(nums, element, i+1)

def LastOccurence(nums, element, i):
    if i == len(nums):
        return -1
    if nums[i] == element:
        ans = FirstOccurence(nums,element,i+1)
        if ans == -1:
            return 1
        else:
            return ans
    else:
        return FirstOccurence(nums,element,i+1)
nums = [10,20,25,40,20]
element = 200
print(FirstOccurence(nums,element,0))
print("Last Occurence of", element, "is",LastOccurence(nums, element, i))