#getting the input from file
f = open('rosalind_iprb.txt')

#reading the line and getting the dnas
line1 = f.readline()

#getting the values of k,m and n
values = line1.split()
k = int(values[0])
m = int(values[1])
n = int(values[2])

#total
t = k+m+n

#since the probability is multiplicative when two events' probability is taken
#hence the variable are define as
#for eg km means the probability of randomly picking m after picking a k individual
kk = (k/t)*((k-1)/(t-1))
km = (k/t)*(m/(t-1))
kn = (k/t)*(n/(t-1))

mm = (m/t)*((m-1)/(t-1))
mk = (m/t)*(k/(t-1))
mn = (m/t)*(n/(t-1))

nn = (n/t)*((n-1)/(t-1))
nk = (n/t)*(k/(t-1))
nm = (n/t)*(m/(t-1))

#adding all the matings that produce homozygous or heterozygous dominant
print(round((kk + km + kn + mk + 0.75*mm + 0.5*mn + nk + 0.5*nm),5))
