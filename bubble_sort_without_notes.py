def bubble_sort(nums: list[int]):
    end = len(nums)
    swapping = True

    while swapping:
        swapping = False

        for i in range(1, end):
            if nums[i - 1] > nums[i]:
                nums[i - 1], nums[i] = nums[i], nums[i - 1]
                swapping = True


        end -= 1


my_list = [23, 576, 76, 12, 976, 345]
bubble_sort(my_list)
print(my_list)
