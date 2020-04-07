def to_sum(num) :
    a_num = 1
    sum_so_far = 0

    while a_num <= num :
        sum_so_far += a_num
        a_num += 1
    return sum_so_far

print(to_sum(4))