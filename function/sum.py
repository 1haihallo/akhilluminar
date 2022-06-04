
def sum_numbers(n1,n2):
    return n1+n2
print(sum_numbers(10,20))

def sub_numbers(n1,n2):
    return n1-n2
print(sub_numbers(10,20))

def smart_sub(n1,n2):
   return n1-n2 if n1>n2 else n2-n1
print(smart_sub(5,10))

def num_chk(num):
   return "even" if num%2==0 else "odd"
print(num_chk(15))

def validate_gmail(gmail):
   return gmail.endswith("@gmail.com")
print(validate_gmail("abc@gmail.com"))

#create a number that will return factorial
def factorial (num):
    fact=1
    for i in range (1,num+1):
       fact=fact*i
    return fact
print(factorial(3))

sub=lambda n1,n2:n1-n2
print(sub(10,20))


smart_sub=lambda n1,n2:n1-n2 if n1>n2 else n2-n1
print(smart_sub(5,10))



