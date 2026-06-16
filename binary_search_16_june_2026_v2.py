def binary_search(sorted_nums: list[int], my_key: int) -> int:
    start = 0
    end = len(sorted_nums) - 1

    while start < end:
        mid = (start + end) // 2

        if nums[mid] == my_key:
            return mid

        if nums[mid] < my_key:
            start = mid + 1

        if nums[mid] > my_key:
            end = mid - 1

    return -1 


print(binary_searc([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 6)
