def binary_search(nums: list[int], my_key: int) -> int:
    low = 0
    high = len(nums) - 1

    while low <= high:
        mid = (low + high) // 2

        if nums[mid] == my_key:
            return mid

        if nums[mid] < my_key:
            low = mid + 1

        if nums[mid] > my_key:
            high = mid - 1
    
    return -1


my_index = binary_search([1, 2, 4, 67, 89, 100, 120, 150], 1)
print(my_index)
