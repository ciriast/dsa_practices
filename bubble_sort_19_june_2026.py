def bubble_sort(nums: list[int]) -> list[int]:
    swapping = True
    end = len(nums)

    while swapping:
        swapping = False

        for i in range(1, end):
            if nums[i - 1] > nums[i]:
                nums[i - 1], nums[i] = nums[i], nums[i - 1]
                swapping = True

        end -= 1
    
    return nums

print(bubble_sort([199, 377, 12, 998, 344, 91, 34, 566, 722, 643, 861, 971]))
