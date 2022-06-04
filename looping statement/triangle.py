    *
  *    *
 *   *   *
*  *   *   *
#n=5
#for r in range(0,5):
  #  for c in range(0,n-r-1):
   #     print(end=" ")
    #for c in range(0,r+1):
     #   print("* ",end='')
    #print()
#hollow pyramid
for row in range(1,5):
    for col in range(1,7):
        if row==4 or row+col==4 or col-row==2:
            print("*",end='')
        else:
            print(end=" ")
    print()