#lists indexes
myList =[1,2,3,"A"]
print (myList)
print (myList[2])

#slicing lists
languages = ["C++","C#","Java","Html","Rails"]
print(languages[2:4])
print(languages[1:])
print(languages[:])

# add element in list (append())
names=["jack","peter","jane","Mercy"]
print("Before appending:", names)
names.append("Mwiti")
print("After Appending: ", names)

#add list to another (extend)

vowelSounds =["a","e","i","o","u"]
otherSounds = ["w","v","l"]
print("vowels are:",vowelSounds,"othersare:", otherSounds)
otherSounds.extend(vowelSounds)
print ("After extending:",otherSounds)
#changing values
otherSounds[0]="z"
print(otherSounds)
#remove item from the list
del otherSounds[1:2]
print(otherSounds)
#remove eith the element name
otherSounds.remove("z")
print(otherSounds)
#Iterating through list
for others in otherSounds:
    print(others)
#compressing in the list(increase by the power of two)
otherSound = [other*other for other in range(1,8)]
print(otherSound)