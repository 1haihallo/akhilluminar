

def max_fun(*args):
    return max(args)
print(max(20,30))

def add(*args):
    return sum(args)
print(add(10,20))

def al_details(**kwarg):
    print(sum([v for  v in kwarg.values()])) #  print(sum([v for k, v in kwarg.items()]))

al_details(n1=10,n2=20,n3=30)
def some(**kwargs):
    print(kwargs)
some(name="akhil",bloodgroup="o+",age="29")

dic={"k1":10,"k2":"name","k3":True}

for k,v in dic.items():
    print (k,v)
for v in dic .items():
    print(v)

dic.pop("k3")
print(dic)
