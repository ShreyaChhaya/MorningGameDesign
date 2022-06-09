#Shreya Chhaya 
#We are goign to learn about lists, functions related to lists 
#learn about for loop 
import random #allows you to get random values
import os
os.system('cls')

#lists
thislist= ['apple', 'banana', 'cherry', 'orange', 'melon', 'mango']
print(thislist[1]) #prints banana-number1 on list
print(thislist[-1]) #prints cherry-last one on list
print(thislist[-3]) #prints apple-counting backwards
print(thislist[2:5]) #prints multiple elements- will format the print with brackets and apostrophe
print(thislist[:3]) #prints everythign up to 3 not including 3
print(thislist[2:]) #prints 2 and everything after 2
print(thislist[-4:-1]) #list starting from back of list- gives -4 to -2, not including -1

if 'apple' in thislist:
    print('yes, apple is in the list') #can do if then statements with objects in list 
else:
    print('not in list')

#for loop
#'for' and then a variable name 
for num in range(10):
    print(num) #gives list 0-9 becasuse printing numbers with limit of 10

for element in thislist:
    print(element) #prints all the elements in the list

for element in thislist: #element=thislist[times run through loop]
    print(element, end=" ")

thislist.append("pinaple") #adds elements to end of the list 
print(thislist[0:]) #adds pinaple ot the existing list

for num in range(2):
    thislist.append(input('input a food '))

#insert
thislist.insert(0, 'pinaple') #putting pinaple at 0 on list
print(thislist[0:]) #adds an element to a specifiic index in list

for i in range(len(thislist)): #prints entire list
    print(thislist[i], end='/') #slash prints with slash in between each word-no brakets or apostrophes

list2=[1, 2, 3, 4] 
list2.extend(thislist) #adds list2 to thislist
print(list2)


word=random.choice(thislist) #picks random element from the list
print(word)

guess = input('input a food')
if guess in word:
    print('congrats, you guessed the food')
