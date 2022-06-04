#1234
#1234
#1234
#for row in range(1,5):
    #for col in range(1,5):
        #print(col,end="")
    #print()
#1 1 1
#2 2 2
#3 3 3
#4 4 4
#for col in range(1,4):
    #for row in range(1,5):
      #  print (row,end="")
    #print()
#1
#1 2
#1 2 3
#1 2 3 4
#for row in range(1,5):
 #   for col in range(1, row+1):
  #      print(col, end="")
   # print()
# 1
# 2 2
# 3 3 3
# 4 4 4 4

for col in range(1,5):
    for row in range(1,col+1 ):
        print(col, end="\t ")
    print()
####
###
##
#
#for row in range(1,5):
    #for col in range(5, row,-1):
     #   print("*", end="")
    #print()