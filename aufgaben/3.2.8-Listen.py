def get_evens(nums):
    evens = []
    for num in nums:
        if num % 2 == 0:
            evens.append(num)
    return evens

print(get_evens([4, 7, 2, 9, 1, 5, 3]))
