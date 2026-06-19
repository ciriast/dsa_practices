def binary_search(nums: list[int], my_key: int) -> int:
    start = 0
    end = len(nums) - 1

    while start <= end:
        middle = (start + end) // 2

        if nums[middle] == my_key:
            return middle

        if nums[middle] < my_key:
            start = middle + 1

        if nums[middle] > my_key:
            end = middle - 1
    
    return -1

print(binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 1))
