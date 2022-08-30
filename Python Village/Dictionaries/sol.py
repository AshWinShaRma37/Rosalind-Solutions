#getting the input from file
f = open('rosalind_ini6.txt','r')

#reading the line and getting the string
line = f.read()

#getting the string
#stripiing to avoid unneccessary spaces at start and end
words = (line.strip()).split(' ')

#creating an empty dictionary
#dictionary will contain words : counts
dic = {}

for word in words:
         #if the word is seen for the first time add it in dictionary
         if word not in dic:
                  dic[word]=1
         #if the word has already been added to dictionary add it's count
         else:
                  dic[word]=dic[word]+1

for key, value in dic.items():
    print(key,value)
