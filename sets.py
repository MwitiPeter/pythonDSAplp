#sets for difrent types
student_id = {112,113, 114,115,115}
print('StudentsId:',student_id)

#create an empty set
emptySet = set()
print ('Data type:',type(emptySet))
emptyDict = { }
print ('Data type:', type(emptyDict))
#printing a duplicate value
print(student_id)
#adding a set 
student_id.add(118)
print('updated:',student_id)
#update two sets
student_age = {13,24,23,12,34}
student_id.update(student_age)
print(student_id)
#remove value froma set
student_id.discard(34)
print(student_id)

#iterate overt the sets
for ids in student_id:
    print (ids)
# sets length number of elements
print(len(student_id))   