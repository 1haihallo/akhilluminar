class parent:
    def mobile(self):
        print("moto g5")
    def bike(self):
        print("ather")

class child(parent):    #inherit
    pass
ch=child()
ch.mobile()
ch.bike()

####overriding#######


class parent:
    def mobile(self):
        print("moto g5")
    def bike(self):
        print("ather")

class child(parent):
    def mobile(self):
        print("iphone13")
    def bike(self):
        print("duke")

ch=child()
ch.mobile()
ch.bike()