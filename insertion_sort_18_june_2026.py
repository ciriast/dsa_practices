def insertion_sort(nums: list[int]) -> list[int]:
    start = 1
    end = len(nums)

    for i in range(start, end):
        j = i

        while j > 0 and nums[j - 1] > nums[j]:
            nums[j - 1], nums[j] = nums[j], nums[j - 1]
            j -= 1

    return nums

my_sorted_list = insertion_sort([60, 19, 345, 89, 9, 76, 21, 26, 777, 129, 52, 23, 72, 999, 222, 333, 1])
print(my_sorted_list)
