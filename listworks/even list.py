lst=[1,2,3,4,5,6,7,8,9,2,2,2,]
print(lst.count(2))
evenlst=[]
for num in lst:
    if num%2==0:
        evenlst.append(num)
print(evenlst)
evenlst.sort(reverse=True)
print(evenlst)
lst.insert(5,10)
print(lst)

lst1=[10,11,12,13,14]
lst2=[11,12,13,140,18]
newlst=[]
for num in lst1:
    if num in lst2:
        newlst.append(num)
print(newlst)
#most frequent element
lst=[1,2,3,1]
# from statistics import mode
# print(mode(lst)
# def most_feq():
#     count=0
#
#     for i in lst:
#         occurence=lst.count(i)
#         if occurence>count :
#             count=occurence
#             num=i
#     return(num)
# print(most_feq())
# dup_lst=[]
# for i in range(0,len(lst)):
#     for j in range(i+1,len(lst)):
#         if lst[i]==lst[j]:
#             dup_lst.append(lst[i])
#             print(dup_lst)
list=[2,3,5,6,4]
sum=8
# for i in range (0,len(list)):
#     for j in range (i+1,len(list)):
#         sum_list=list[i]+list[j]
#         if sum == sum_list:
#             print(f"pairs = {list[i]},{list[j]}")
#             break
list.sort()
low=0
upp=len(list)-1
while(low<upp):
    curr_sum=list[low]+list[upp]
    if curr_sum == sum:
        print(f"pairs={list[low]},{list[upp]}")
        break
    elif curr_sum > sum:
        upp-=1
    elif curr_sum < sum:
        low+=1
