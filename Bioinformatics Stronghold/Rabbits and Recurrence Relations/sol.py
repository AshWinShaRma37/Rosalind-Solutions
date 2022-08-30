#defining the function
def rabbits(n, k):
         #having 2 variables initially to be 1
         prev1 = 1
         prev2 = 1
         for i in range(2, n):
                  # from previous rabbit population getting new month population
                  current = prev1 + k * prev2
                  #changing the prev to store the old and current values
                  prev2 = prev1
                  prev1 = current
         return current

#getting the input from file
f = open('rosalind_fib.txt','r')

#reading the line and getting the string
line1 = f.readline()

#getting the values of n and k
values = line1.split()
n = int(values[0])
k = int(values[1])

print(rabbits(n,k)) 
