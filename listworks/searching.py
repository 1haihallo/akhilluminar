arr=[1,5,1,2,30,50,40,80,90]
element=100
flag=0
#for n in arr:
   # if element==n:
  #      flag=1
 #       break
#print('element found' if flag==1 else 'element not found')
for i in range(0,len(arr)):
    if element==arr[i]:
        flag=1
        break
print('element found' if flag==1 else 'element not found')