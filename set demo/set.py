ldt=[10,20,30,10,10,20,30]
st=set(ldt)
print(st)

st1={1,2,3,5,7}
st2={1,3,9,11,5,13}
union_st=st1.union(st2)
print(union_st)

intersection_set=st1.intersection(st2)
print(intersection_set)

difference_set=st1.difference(st2)
print(difference_set)

students=['ram','ravi','hari','tom']
passed_students=['ram','ravi','hari']
failed_stud=set(students).difference(set(passed_students))
print(failed_stud)