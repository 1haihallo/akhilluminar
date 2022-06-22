lst=[
    [10,15],
    [13,19],
    [60,70],
    [40,30],
    [9,13]
]
# for sub_lst in lst:
#     for num in sub_lst:
#         num>16
#         print(num)

fltn_lst=[num for slist in lst for num in slist]
print(fltn_lst)

num_grt_sixt=[num for num in fltn_lst if num>16]
print(num_grt_sixt)

odd_num=[num for num in fltn_lst if num %2 !=0]
print(odd_num)

sum_of_even=sum([num for num in fltn_lst if num %2 ==0])
print(sum_of_even)

increase_num=[num+1 if num>25 else num-1
              for num in fltn_lst] #mapped number
print(increase_num)
