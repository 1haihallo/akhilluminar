#num=10
#num1=20
#if(num>num1):
  #  print(f'{num} is the largest')
#else:
   # print(f'{num1} is the largest')
num=123#1**3 +2**3+ 3**3
sum=0
while(num!=0):
    digit=num%10
    cube=digit**3
    sum=cube+sum
    num=num//10
print(sum)

