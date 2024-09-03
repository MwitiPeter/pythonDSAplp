capitalCity = {"Kenya":"Nairobi","Uganda":"Kampla","England":"London"}
print(capitalCity)
#"Key":"Value"
capitalCity["Tanzania"] ="Dodoma"
print(capitalCity)
#deleting keys
del capitalCity["Tanzania"]
print(capitalCity)
print(capitalCity["England"])

#dictionary mebership test
dictNumber ={1:1,3:5,4:6,8:9}
print(1 in dictNumber, 7 in dictNumber)
#iterating throught the values of the keys
for i in dictNumber:
    print(dictNumber[i])
    