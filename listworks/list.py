football=['messi','ronaldo','neymar','pele','maradona']
##for name in football:
   # print(name)
for i in range(0,len(football)):
    print(football[i])

numbers=[10,13,15,18,20]
for num in numbers:
   if num%2==0:
        print(num)


numbers=[10,13,15,18,20]
for num in numbers:
    if num>15:
        print(num+1)
    elif num<15:
        print(num-1)
    elif num==15:
        print(num)
count=0
for num in numbers:
      if num in range(14,19):
          count+=1
          print(count)

numbers=[-1,2,2,3,0,-5,0,-1,2,3,0]
count=0
coun=0
cou=0
for num in numbers:
    if num>0:
        count+=1

    elif num<0:
        coun+=1

    elif num==0:
        cou+=1
print(f"+ve count={count}, -ve count={coun},zero count={cou}")
arr=[1,5,1,2,30,50,40,80,90]
element=40
for n in arr:
    print("element found" if element == n else "element not found")
numbers=[-1,2,2,3,0,-5,0,-1,2,3,0]
sum=0
sums=0
for n in numbers:
    if n>0:
        sum=sum+n
    elif n<0:
        sums=sums+n
print(f"+ve numbers sum={sum}")
print(f"-ve numbers sum={sums}")


