def tally(nums:list[int]) -> int:
    total = 0
    for num in nums:
        total = total + num           #total = 16 and num =1
    return total

result = tally([4, 9, 2, 1])
print(result)




def copy(nums:list[int]) -> list[int]:
    new_list = []
    for idx in range(len(nums)):
        new_list.append(nums[idx])     # new_list= [4, 9, 2, 1] idx=3
    return new_list                    # it uses the length of the list to copy it to another list

result = copy([4, 9, 2, 1])
print(result)




def increment_all(nums:list[int]) -> list[int]:
    new_list = []
    for value in nums:
        new_list.append(value + 1)     # new_list = [5, 10, 3, 2] value = 1
    return new_list

result = increment_all([4, 9, 2, 1])
print(result)