#importing biopython
from Bio import SeqIO
from Bio.SeqUtils import GC

#getting the input from file
f = open('rosalind_fib.txt','r')

#dictionary to contain seq name and gc content
dna = {}

#reading each fasta and storing the gc content
for f in SeqIO.parse('rosalind_gc.txt', 'fasta'):
    dna[f.id] = GC(f.seq)

#using max function to get the max gc seq
print(max(dna, key=dna.get))
print(dna[max(dna, key=dna.get)])
