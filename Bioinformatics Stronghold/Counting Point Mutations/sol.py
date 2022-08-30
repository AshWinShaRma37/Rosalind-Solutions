#getting the input from file
f = open('rosalind_hamm.txt')

#reading the line and getting the dnas
dna1 = f.readline()
dna2 = f.readline()

# initial distance set to 0
hd = 0
for nt1 , nt2 in zip(dna1 , dna2):
  if nt1 != nt2:
    hd += 1 #increasing if the nucleotides are not equal
print(hd)
