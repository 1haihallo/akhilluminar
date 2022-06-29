from blog.models import users,posts
session={}
def signin_req(fn):
    def wrapper(*args,**kwargs):
        if "user" in session:
            return fn(*args,**kwargs)
        else:
            print("invalid session")
    return wrapper


def authenticate(**kwargs):
    username=kwargs.get("username")
    password=kwargs.get("password")
    user = [user for user in users if user["username"] == username and user["password"] == password]
    return user
# print(authenticate(username="akhil",password="Password@123"))
class loginview:
    def post(self,*args,**kwargs):
        username=kwargs.get("username")
        password=kwargs.get("password")
        user=authenticate(username=username,password=password)
        if user:
            session["user"]=user[0]
            print(session)
class postlistview:
    @signin_req
    def get(self,*args,**kwargs):
        return posts
class mypostlistview:
    @signin_req
    def get(self, *args, **kwargs):
        userId=session["user"]["id"]
        my_post=[post for post in posts if post["userId"]==userId]
        return my_post



log_in=loginview()
log_in.post(username="nik   il",password="Password@123")
all_post=postlistview()
mypost=mypostlistview()
print(mypost.get())

