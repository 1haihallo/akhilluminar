def is_prime(num):
    res=False
    if num>1:
        for i in range(2, num):
           if (num % i == 0):
                return res
        else:
            res=True
    return res

print(is_prime(9))
#def is_prime(num):
 #   flag=0
  #  for i in range(2,num):
   #     if (num%i == 0):
    #        flag=1
     #       break
    #return True if flag==0 else False
#print(is_prime(9))
#def prime_range(low,upp):
 #   for num in range(low,upp+1):
          #  if prime_range(num)
  #         print(num)
#prime_range(35,50)
