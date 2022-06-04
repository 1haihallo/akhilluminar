num=2
i=1
res=0 #pattern=""
add=0
while(i<=num):
    res=res*10+num #pattern=pattern+str(num)
    add=add+res
    i+=1
print(add)