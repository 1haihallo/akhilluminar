cinema={'film':'hridayam','quality':'hd','hero':'pranav','year':'2020','ticket':150}
print(cinema["film"])
print(cinema["year"])
print('heroine'in cinema)
cinema['heroine']='kalyani'
print(cinema)
account={"name":"akhil","type":"current","open":"2020"}
print(account["name"])
print("balence" in account)
account["balance"]=10000
print(account)
account["balance"]+=2000
print(account)
print(cinema.get("year"))
print(cinema.get("quality"))
if "release" in cinema:
    cinema["release"]='ott'
else:
    cinema["release"]="theatre"
print(cinema)
if cinema['ticket'] >200:
    cinema['ticket']-=10
else:
    cinema['ticket']+=10
print(cinema)