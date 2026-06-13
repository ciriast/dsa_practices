def insertion_sort(nums: list[int]) -> list[int]:
    nums_len = len(nums)

    for i in range(1, nums_len):
        j = i

        while j > 0 and nums[j-1] > nums[j]:
            nums[j - 1], nums[j] = nums[j], nums[j - 1]
            j -= 1
    
    return nums


my_ordered_list = insertion_sort([38, 577, 4739, 122, 977, 2, 588, 8, 727, 44, 612])
print(my_ordered_list)
