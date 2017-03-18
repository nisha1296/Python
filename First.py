#The word which occurs the most number of times
name=raw_input("Enter the file name: ")
handle=open(name,'r')
text=handle.read()
words=text.split()

counts=dict()
for word in words:
  counts[word]=counts.get(word,0)+1
print(counts)  
bigcount=0
bigword=0

for word,count in counts.items():
    if count>bigcount:
        bigword = word
        bigcount = count
print bigword, bigcount  
