mobiles = [
    [1000, "samsungA52", "4g", "AMOLED", 27000, "samsung", 12],
    [1001, "samsungA52s", "5g", "AMoLED", 32000, "samsung", 20],
    [1002, "redminote10", "4g", "led", 17000, "redmi", 50],
    [1003, "redminote11pro", "5g", "superAMOLED", 20000, "redmi", 70],
    [1004, "samsungA72", "5g", "AMOLED", 27000, "samsung", 1],
    [1005, "samsungA53", "5g", "AMOLED", 27000, "samsung", 34],
    [1006, "samsungm52", "5g", "AMOLED", 27000, "samsung", 7],
    [1007, "samsungm53", "5g", "AMOLED", 27000, "samsung", 89],
    [1008, "samsungA22", "5g", "AMOLED", 27000, "samsung", 0],
    [1009, "iphone13", "5g", "AMOLED", 97000, "apple", 0],
    [1010, "oneplusnordce2", "5g", "AMOLED", 23000, "oneplus", 67]

]
# q1 total number of out_of_stock
#
# out_of_stocks=[mob for mob in mobiles if mob[6]== 0]
# print (out_of_stocks)

# q2 total stock
# total_stock=sum([mob[-1]for mob in mobiles])
# print(total_stock)

# q3 pritn mobiles available in range 20k to 30k
# greater_than=[mob for mob in mobiles if mob[4]>=20000 and mob[4]<=30000]
# print(greater_than)
# greater_than=[mob for mob in mobiles if mob[4] in range (20000,30000)]
# print(greater_than)


# q4 print all 5g phone
# five_g=([mob for mob in mobiles if mob[2]=='5g'])
# print(five_g)

# q5 print samsung mobiles


# q6 print costly mobile
# high_price=max([mob[4] for mob in mobiles])
# print(high_price)
# mobiles.sort(reverse=True,key=lambda mob:mob[4])
costly=max(mobiles,key=lambda m:m[4])
print(costly)

# q7 prin low cost mobiles
low_cost=min(mobiles,key=lambda m:m[4])
print(low_cost)


# q8 print all mobiles having stock >10
stocks=[mob for mob in mobiles if mob[6]>10]
print (stocks)

# q9 count of mobiles having dispaly amoled
amoled=([mob for mob in mobiles if mob[3]=='AMOLED'])
print(amoled)

# q10 sort mobiles based on price oredr by desc
mobiles.sort()

# q11 sort mobiles based on avl stock oredr by desc

# q12 is there any mobile available at rs 10000 ?
MOB_TEN=[mob[4]==10000 for mob in mobiles]
print('available' if True in MOB_TEN else 'na')

# q12 list all mobiles having same price
