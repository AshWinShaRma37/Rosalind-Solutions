#getting the input from file
f = open('rosalind_ini4.txt')

#reading the line and getting the string
line1 = f.readline()

#getting the values
values = line1.split()
a = int(values[0])
b = int(values[1])

#creating a variable to store sum of odd integers:
s = 0

#creating a loop to find all odd integers and adding them to sum
for i in range(a,b+1):
         if i % 2 ==1:
                  s=s+i

#printing the result
print(s)

#another method
#using range with step of 2 to get all the odd integers
#used a|1 to make sure range starts from an odd integer
print(sum(range(a|1,b+1,2)))
