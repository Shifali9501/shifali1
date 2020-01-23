students=["john","jennie"]
print(students,hex(id(students)))
newStudents=students + ["fionna"]
print(newStudents,hex(id(newStudents)))
students= students + ["fionna"]
print(students, hex(id(students)))