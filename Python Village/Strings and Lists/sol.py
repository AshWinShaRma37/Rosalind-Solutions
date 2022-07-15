#getting the input from file
f = open('rosalind_ini3.txt')

#reading the line and getting the string
line1 = f.readline()

#and the indices
line2 = f.readline()
values = line2.split()
a = int(values[0])
b = int(values[1])
c = int(values[2])
d = int(values[3])

#printing the required text
print(line1[a:b+1], line1[c:d+1])
