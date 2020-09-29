'''
Author Name: Amit Kumar
Python version: Python 3.5 7 above

''


n=int(input())#enteries in phonebook
phonebook = dict()
for i in range(n):
    line=input()
    line=line.split()
    phonebook[line[0]]=phonebook.get(line[0],line[1])

while 1:
    try:
        q=input()
        if q in phonebook:
            print(str(q) + "=" + str(phonebook[q]))
        else:
            print("Not found")
    except:
        break

'''
        n = int(input())#total number of inputs to be searcged and inpuytted as well
phonebook = dict()#dictionary fx use kiya h basically it has converted phone book as a dictionary to find inputs recieved
for i in range(n):
    line = input()#yad rakhio dono name and phone number isi me daal diya h lauda
    line = line.split()#aur yha pe aa kr ke usko split kr ke array bna rha h to badically wo split ho kr ke 0th position pe alag and 1str position pe alag value de rha h 
    phonebook[line[0]] = phonebook.get(line[0],line[1])#ab yha pe line(0) ko check kr rha h means oth posioton pe we have inputted name so it is checking the name whether wo match kr rha hki nahi if it matched then agae......
#get function is used to assign value 
while 1:
    try:#check the code for errors
        q = input()
        if q in phonebook:
            print(str(q) + "=" + str(phonebook[q]))
        else:
            print("Not found")
    except:#is used to resolve the errors
        break
    '''


