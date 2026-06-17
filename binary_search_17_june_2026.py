def binary_search(sorted_nums: list[int], key: int) -> int:
    start = 0
    end = len(sorted_nums) - 1

    while start <= end:
        mid = (start + end) // 2

        if sorted_nums[mid] == key:
            return mid

        if sorted_nums[mid] < key:
            start = mid + 1

        if sorted_nums[mid] > key:
            end = mid - 1

    return -1


print(binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 9))
