''''Question 12
Level 2

Question:
Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each digit of the number is an even number.
The numbers obtained should be printed in a comma-separated sequence on a single line.

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.'''

ciag = [liczba for liczba in input().split(sep=",") ]

wynik = []
for i in range(len(ciag)):
    if int(ciag[i]) >= 1000 and int(ciag[i]) <=3000 and int(ciag[i][0])%2==0 and int(ciag[i][1])%2==0 and int(ciag[i][2])%2==0 and int(ciag[i][3])%2==0:
        wynik.append(ciag[i])

print(wynik)
