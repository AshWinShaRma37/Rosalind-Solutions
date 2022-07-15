#getting the input from file
f = open("rosalind_ini2.txt", "rt")
#reading the line and getting the two integers
line = f.read()
values = line.split()
a = int(values[0])
b = int(values[1])
#printing the hypotenuse of these numbers
print(a**2 + b**2)

#closing the opened file
f.close()
