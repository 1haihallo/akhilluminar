class course:
    def add_course(self,**kwargs):
        self.course_name = kwargs.get("course_name")
        self.status = kwargs.get("status")

    def __str__(self):
        return self.course_name
class batch:
    def add_batch(self,**kwargs):
        self.course = kwargs.get("course")
        self.b_code = kwargs.get("b_code")
        self.date = kwargs.get("date")

    def __str__(self):
        return self.b_code


class student:
    def add_student(self,**kwargs):
        self.name = kwargs.get("name")
        self.gender = kwargs.get("gender")
        self.id = kwargs.get("id")
        self.batch = kwargs.get("batch")

    def __str__(self):
        return self.name

django=course()
django.add_course(course_name="django",status=True)
bigdata=course()
bigdata.add_course(course_name="bigdata",status=True)

db1=batch()
db1.add_batch(course=django,b_code="djmay2022",date="18-8-2022")
bd1=batch()
bd1.add_batch(course=bigdata,b_code="bdmay2022",date="18-8-2022")


lal=student()
lal.add_student(name="lal",gender="male",id="12364",batch=db1)
sachin=student()
sachin.add_student(name="sachin",gender="male",id="12364",batch=db1)
rohit=student()
rohit.add_student(name="rohit",gender="male",id="12364",batch=db1)

print(lal.batch.course.course_name)
