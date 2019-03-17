'''
Question:
Define a class which has at least two methods:
getString: to get a string from console input
printString: to print the string in upper case.
Also please include simple test function to test the class methods.'''

class zadanie():
    def __init__(self):
        self.tekst = ""
    def getString(self):
        self.tekst = input()

    def printString(self):
        print(self.tekst.upper())


a= zadanie()
a1 = a.getString()
b1 = a.printString()