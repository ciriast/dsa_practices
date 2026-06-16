def quick_sort(nums: list[int], start: int, end: int) -> None:
    if end <= start:
        return

    mid = partion(nums, start, end)

    quick_sort(nums, start, mid - 1)
    quick_sort(nums, mid + 1, end)

def partion(nums: list[int], start: int, end: int) -> int:
    pivot = nums[end]
    i = start - 1

    for j in range(start, end):
        if nums[j] < pivot:
            i += 1
            nums[i], nums[j] = nums[j], nums[i]

    nums[i + 1], nums[end] = nums[end], nums[i + 1]

    return i + 1


my_nums = [18, 12, 2, 4, 6, 7, 800, 17]
quick_sort(my_nums, 0, 7)
print(my_nums)

