num=123#1**3 +2**3+ 3**3 #armstrong
sum=0
while(num!=0):
    digit=num%10
    cube=digit**3
    sum=cube+sum
    num=num//10
print(sum)