# class staff:
#     id:int
#     name:str
#     role:str
#     def __init__(self,*args,**kwargs):
#         self.id=kwargs.get("id")
#         self.name=kwargs.get("name")
#         self.role=kwargs.get("role")
#
#     def __str__(self):
#         return self.role
#
# user=staff(id=100,name="ajay",role="admin")
# print(user)

class employee:

    def __init__(self,**kwargs):
        self.e_id=kwargs.get("e_id")
        self.name=kwargs.get("name")
        self.role=kwargs.get("role")

    def __str__(self):
        return self.name

employe=employee(e_id=10012,name="nithin",role="admin")


class dept():
    def __init__(self,**kwargs):
        user=kwargs.get("user")
        if user.role=="admin":
            self.dept_name=kwargs.get("dept_name")
            self.user=kwargs.get("user")
        else:
            print("no access")

    def __str__(self):
        return self.dept_name

dep=dept(dept_name="revenue",user=employe)
print(dep)
print(dep.user)