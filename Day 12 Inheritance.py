class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName #initialization of first number ,last number as done in the constructor
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)# #printout statement
		print("ID:", self.idNumber)
import statistics #for using predefined method statistics to calculate mean
class Student(Person):
    def __init__(self,firstName, lastName, idNumber, scores):#taking the value from main function 
        
        
        super().__init__(firstName, lastName, idNumber)#calling the super class note here tht super is predefined function in python used to initialize child class with super class
        self.scores=scores # assigning the value here to local variable
    def calculate(self): #function defined to calculate the grades
        a = statistics.mean(self.scores) #best way to calculate mean but only for lists/arrays
        if a < 40:
            return "T"
        elif (40 <= a) and (a < 55):
            return "D"
        elif (55 <= a) and (a < 70):
            return "P"
        elif (70 <= a) and (a < 80):
            return "A"
        elif (80 <= a) and (a < 90):
            return "E"
        elif (90 <= a) and (a <= 100):
            return "O"
        else:
            return ""

   

    #   Function Name: calculate
    #   Return: A character denoting the grade.
    #
    # Write your funct
    
line = input().split() #entering the value
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input()) #noy needed for python
scores = list( map(int, input().split()) )
s = Student(firstName, lastName, idNum, scores)#sending the value to class
s.printPerson()
print("Grade:", s.calculate())#recieveing the value and printing the output
