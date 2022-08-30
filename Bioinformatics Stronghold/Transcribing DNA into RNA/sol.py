#getting the input from file
f = open('rosalind_rna.txt','r')

#reading the line and getting the string
line = f.read()

#getting the dna sequence
#stripiing to avoid unneccessary spaces at start and end
dna = line.strip()

#using count to get each nucleotides count
print(dna.replace('T','U'))
