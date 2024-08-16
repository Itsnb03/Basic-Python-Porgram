def remove_d(numbers):
    unique_n=[]
    for num in numbers:
        if num not in unique_n:
            unique_n.append(num)
    return unique_n

nums = [1, 2, 3, 2, 1, 3, 2, 4, 5, 4]
unique=remove_d(nums)
print(unique)