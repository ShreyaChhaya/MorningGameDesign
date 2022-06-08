#shreya chhaya
#files
# r read 
# w write 
# a append

#open files make sure you close the file 
import os, datetime
os.system('cls')
name="Shreya"
score=120

date=datetime.datetime.now() #todays date and time 

print(date.strftime('%m/%d/%Y')) 
print(date.strftime('%Y %m %d')) #can change order

screLine=str(score) + '\t'+name+'\t'+ date.strftime('%m/%d/%Y')
print(screLine)
#to open a file
myFile=open('scre.txt', 'w') #this is goign to open a file to write
myFile.write(screLine)
myFile.close()
#this opens a file on the side with writing in it
myFile=open('scre.txt', 'r') #once the file is closed you can now open it to read
lines=myFile.readlines()
print(lines)
for line in myFile.readlines():
    print(line)
myFile.close()

