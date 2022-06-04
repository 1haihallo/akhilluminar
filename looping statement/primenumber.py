num=10
flag=0
for i in (2,num):
    if (num%i==0):
        flag=1
        break
if(flag==0):
    print('prime')
if(flag==1):
    print('not prime')