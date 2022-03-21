
file_name = input("type the file name: ")
myfile = open(file_name, "r")
print(file_name, "is opened")
text = myfile.read()
wordcounts = []
sentences = text.split('.')
for x in sentences:
    words = x.split(' ')
    wordcounts.append(len(words))
average_wordcount = sum(wordcounts)/len(wordcounts)
myfile.close()
print(file_name, "is closed")
print(average_wordcount)
if average_wordcount < 10:
    print("The text belongs to Hemingway")
else:
    print("The text belongs to Charles Dickens")
    
    



