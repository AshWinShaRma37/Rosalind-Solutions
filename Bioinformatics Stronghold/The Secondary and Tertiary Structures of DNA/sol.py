## Method 1
#using Biopython to solve this 
from Bio.Seq import Seq
#getting the input from file
f = open('rosalind_revc.txt','r')

#reading the line and getting the string
line = f.read()

#getting the dna sequence
#stripiing to avoid unneccessary spaces at start and end
dna = Seq(line.strip())

#using count to get each nucleotides count
print(dna.reverse_complement())

## Method 2
#using dictionary
dna1 = line.strip()
reverse = {"A" : "T", "T" : "A", "C" : "G", "G" : "C"}
result= ""
for nt in dna1:
         result += reverse[nt]
print(result[::-1])         
