#Shreya Chhaya
#Write a program to create a new string made of an input string’s first, middle, and last character
#worksheet about stings 
import os
os.system('cls')
#get first middle and last letters of name
#question 1:
a = 'James'
print(len(a)) #number of letter, lena finds theamount of letters
print(a[0], end='') #get first letter
print(a[2], end='')
print(a[4]) #put last letter on the same line

word=input('You word is') #get word from user
number = (len(word)) #get the number of letters in the word
first=word[0] #find first letter
middleNumber=int(number/2) #get the nymber of the middle digit in the word
middle= word[middleNumber] #get the middle letter
last=word[number-1] #get last leter
print(first+middle+last) 

#Question 2
word=input('your word is') #get word from user
number= len(word) #get number of letters in word
middle2=number//2 #double division- integer division
middleFirst=word[middle2-1:middle2+2]
print(middleFirst)
#print('The middle three characters are:',word[middle2-1]+word[middle2]+word[middle2+1])

#Question 3
#put one word inside the other, splitting first word in half
word1=input('your word is') #get first word
word2=input('your second word is') #get second word
half1=len(word1)//2 #find first half of the word

print(word1[0:half1]+word2+word1[half1:len(word1)])

#Question 4
#two words- first first middle middle last last
word3=input('your first word is')
word4=input('your second word is')
number1=len(word3)
number2=len(word4)
first1=word3[0]
first2=word4[0]
middle3=number1//2
middle4=number2//2
final3=word3[number1-1]
final4=word4[number2-1]
print(first1+first2+word3[middle3]+word4[middle4]+final3+final4)

#Question 5
word5=input('your word is')
if word5[0].islower():
    print(word5[0])





