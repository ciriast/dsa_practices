def quick_sort(nums: list[int], first: int, last: int) -> None:
    if last >= first:
        return

    mid = partion(nums, first, last)

    left = partion(nums, first, mid- 1)
    right = partion(nums, mid + 1, last)


def partion(nums: list[int], left: int, right: int):
    pivot = nums[right]
    i = left - 1

    for j in range(i, right):
        if nums[j] < pivot:
            i += 1
            nums[i], nums[j] = nums[j], nums[i]

    nums[i + 1], nums[right] = nums[right], nums[i + 1]


    return i + 1

my_nums = [2, 7, 19, 29, 477]
quick_sort(my_nums, 0, 4)
print(my_nums)
    
