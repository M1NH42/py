nums = [1,2,3,4,5,6,7,8,9,0]

new_num = list(map(lambda num : num *3, nums))

print(new_num)

new_nums = list(filter(lambda num : num%2==0, nums))

print(new_nums)