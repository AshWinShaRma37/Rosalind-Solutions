#getting the input from file
f = open('rosalind_dna.txt','r')

#reading the line and getting the string
line = f.read()

#getting the dna sequence
#stripiing to avoid unneccessary spaces at start and end
words = line.strip()

#using count to get each nucleotides count
print(words.count('A'),words.count('C'),words.count('G'),words.count('T'))
