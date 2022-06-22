class student:
    name:str
    rollno:int
    gender:str
    def __init__(self,name,rollno,gender):#    def set_student(self,name,rollno,gender):
        self.name=name
        self.rollno=rollno
        self.gender=gender
    def print_student(self):
        print(self.name,self.rollno,self.gender)
p1=student("akhil",101,"male")
# p1.set_student("akhil",101,"male")
p1.print_student()
class course:
    def __init__(self,**kwargs):
        self.c_name=kwargs.get("c_name")
        self.c_id=kwargs.get("c_id")
        self.c_fee=kwargs.get("c_fee")
    def print_details(self):
        print(self.c_name,self.c_fee,self.c_id)

co=course(c_name="data science",c_id="c10111",c_fee=36000)
co.print_details()