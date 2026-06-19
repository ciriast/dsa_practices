def insertion_sort(nums: list[int]) -> list[int]:
    start = 1
    end = len(nums)
    
    for i in range(start, end):
        j = i

        while j > 0 and nums[j - 1] > nums[j]:
            nums[j - 1], nums[j] = nums[j], nums[j - 1]
            j -= 1
    
    return nums

print(insertion_sort([299, 122, 777, 987, 321, 934, 146, 871]))
