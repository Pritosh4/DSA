# You are given list of numbers, obtained by rotating a sorted list an unknown number of times. Write a function to determine the minimum number 
# of times the original sorted list was rotated to obtain the given list. Your function should have the worst-case complexity of O(log N), 
# where N is the length of the list. You can assume that all the numbers in the list are unique.

# Example: The list [5, 6, 9, 0, 2, 3, 4] was obtained by rotating the sorted list [0, 2, 3, 4, 5, 6, 9] 3 times.

# We define "rotating a list" as removing the last element of the list and adding it before the first element. 
# E.g. rotating the list [3, 2, 4, 1] produces [1, 3, 2, 4].

#"Sorted list" refers to a list where the elements are arranged in the increasing order e.g. [1, 3, 5, 7].

# Sample test cases 
# A list of size 5 rotated 3 times. nums=[3,4,5,1,2] 
# A list of size 8 rotated 5 times. nums=[4,5,6,7,8,1,2,3] 
# A list that wasn't rotated at all. nums=[1,2,3,4]
# A list that was rotated just once. nums=[4,1,2,3]
# A list that was rotated n-1 times, where n is the size of the list.nums=[2,3,4,1]
# A list that was rotated n times (do you get back the original list here?) nums=[1,2,3,4]
# An empty list. nums=[]
# A list containing just one element. nums=[1]

# The number of times it is rotated is equal to the position of the lest number of the array
# Concept is that to find the least element using Binary search , we decide whether the element is on the right or the left by comparing the  
# mid element with the last element and seeing if it is less than that element or not since the array is sorted initially.

def search(nums):
    low,high=0,len(nums)
    while low<=high:
        mid=(low+high)//2
        if mid>0 and nums[mid]<nums[mid-1]:
            return mid
        elif mid>0 and nums[mid]>nums[len(nums)-1]: #least element lies on the right side
            low=mid+1
        else: #element lies on the left side
            high=mid-1
    return 0

nums=[1]
result=search(nums)
print(result)
