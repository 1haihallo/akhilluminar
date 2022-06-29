def smart_sub(fn):

    def inner_fn(n1,n2):
        if n2>n1:
            (n1,n2)=(n2,n1)
        return (n1,n2)
    return smart_sub
@smart_sub
def sub(n1,n2):
    return n1-n2
@smart_sub
def div(n1,n2):
    return n1/n2

print(sub(10,20))
print(div(10,2))