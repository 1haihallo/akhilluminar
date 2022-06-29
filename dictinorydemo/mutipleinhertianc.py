   ###muti level inheritance####

class P1:
    def m1(self):
        print("inside p1")
class P2(P1):
    def m2(self):
        print("inside p2")
class P3(P2):
    def m3(self):
        print("inside p3")
p3=P3()
p3.m3()
p3.m2()
p3.m1()

    ###mutiple inheritance####

class P1:
    def m1(self):
        print("inside p1")
class P2:
    def m2(self):
        print("inside p2")
class P3(P2,P1):
    def m3(self):
        print("inside p3")
p3=P3()
p3.m3()
p3.m2()
p3.m1()
