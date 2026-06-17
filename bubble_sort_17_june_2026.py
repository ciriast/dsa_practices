def bubble_sort(nums: list[int]) -> list[int]:
    nums_len = len(nums)
    swapping = True

    while swapping:
        swapping = False

        for i in range(1, nums_len):
            if nums[i - 1] > nums[i]:
                nums[i - 1], nums[i] = nums[i], nums[i - 1]
                swapping = True

        nums_len -= 1

    return nums


print(bubble_sort([6, 878, 22, 76, 52, 89, 12, 7777, 234, 8, 999]))
