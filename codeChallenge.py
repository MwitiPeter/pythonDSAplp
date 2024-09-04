#question 1
userInput = input("Enter a list of integers separated with spaces:")
userInteger = [int(num) for num in userInput.split()]
sum = sum(userInteger)
print (f"The sum is:",sum)

#question 2
tuple1 = ("HarryPoter", "The franchise","Intruder")

for book in tuple1:
    print(book)

#question 3
userInformation = input("Enter your name , age, and favourite color separated with commas")

name, age,  favcolor =[item.strip() for item in userInformation.split(',')]
person_info = {
    "name": name,
    "age": age,
    "favcolor": favcolor
}
print("\npersons info is:")
for key, value in person_info.items():
    print(f'"{key}": "{value}"')

#question4
usersSet1 = input("add a sets of integers:")
usersSet2 = input("add a sets of integer:")

set1 = set(map(int, usersSet1.split()))
set2 = set(map(int, usersSet2.split()))
if set1 == set2:
    print('there equal')
else:
    print('not equal')

#question5
list1= ["Eldoret" , "Nairobi"]
list2=["Kisumu" , "Eldoret"]

set1 = set(list1)
set2 = set(list2)

difference = set1 - set2

print("Difference (list1 - list2):", difference)