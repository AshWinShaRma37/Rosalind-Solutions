#getting the input from file
f = open('rosalind_ini5.txt','r')

#i is the index so reading lines which are odd since i=0,1,2,3...
for i, line in enumerate(f):
    if i % 2 ==1:
        print(line)
