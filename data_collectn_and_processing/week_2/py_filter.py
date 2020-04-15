nums = [1,2,3,4,5,6,7,8,9,0]

new_num = list(map(lambda num : num *3, nums))

print(new_num)


# Python offers a more compact and general way to do it, the filter function. 
# filter takes two arguments, a function and a sequence. The function takes one 
# item and return True if the item should. It is automatically called for each item 
# in the sequence. You don’t have to initialize an accumulator or iterate with a for loop.

new_nums = list(filter(lambda num : num%2==0, nums))

print(new_nums)