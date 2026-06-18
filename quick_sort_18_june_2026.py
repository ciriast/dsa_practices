def quick_sort(nums: list[int], start_index: int, end_index: int) -> None:
    if end_index <= start_index:
        return

    pivot = partion(nums, start_index, end_index)

    left = quick_sort(nums, start_index, pivot - 1)
    right = quick_sort(nums, pivot + 1, end_index)

def partion(nums: list[int], start_index: int, end_index: int) -> int:
    pivot = nums[end_index]
    i = start_index - 1

    for j in range(start_index, end_index):
        if nums[j] < pivot:
            i += 1
            nums[i], nums[j] = nums[j], nums[i]
    
    nums[i + 1], nums[end_index] = nums[end_index], nums[i + 1]

    return i + 1

my_list = [20, 10, 2, 6, 15, 78, 52, 11]
quick_sort(my_list, 0, len(my_list) - 1)
print(my_list)
