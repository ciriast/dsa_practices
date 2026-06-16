def binary_search(nums: list[int], my_key: int) -> int:
    low = 0
    high = len(nums)

    for i in range(1, high):
        mid = (low + high) // 2

        if nums[mid]
