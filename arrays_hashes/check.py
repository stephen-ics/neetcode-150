def binarySearch(array, x, low, high):
    while low <= high:
        mid = low + (high - low)//2
        if array[mid] == x:
            return mid
        elif array[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return False



def containsDuplicate(nums):
    length = len(nums)-1

    nums.sort()

    if len(nums) == 2:
        if nums[0] == nums[1]:
            return True
    elif len(nums) == 1:
        return False

    for elem in nums:
        mid = binarySearch(nums, elem, 0, length)
        if mid >= 0:
            if mid == length:
                if nums[mid-1] == elem:
                    return True
            elif mid == 0:
                if nums[mid+1] == elem:
                    return True
            elif mid != length:
                if nums[mid-1] == elem:
                    return True
                if nums[mid+1] == elem:
                    return True
    return False

arr = [0,4,5,0,3,6]
print(containsDuplicate(arr))
    



