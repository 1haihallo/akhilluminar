class parent:
    def property(self):
        self.prop={"mobile":"nokia3.5","bike":"passion pro"}
        return self.prop
class child(parent):
    def property(self):
        pro=super().property()
        pro["car"]="swift"
        return pro
ch=child()
print(ch.property)
# class editor:
#     def functionality(self):
#         self.func=["create file","execute","save"]
#         return self.func
# class pycharm(editor):
#     def functionality(self):
#         func=super().functionality()
#         func.append(["debug","version control"])
#         return func
# py=pycharm()
# print(py.functionality())