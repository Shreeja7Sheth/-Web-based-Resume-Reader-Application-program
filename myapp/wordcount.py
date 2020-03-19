
filename = "Resume_1.pdf"
numLines = 0
numWords = 0
numChars = 0

with open(filename,'r') as file:
    for line in file:

        wordsList = line.split()
        numLines += 1
        numWords += len(wordsList)
        numChars += len(line)


print(numLines,numWords, numChars)

for p in Document.paragraphs:
    name = p.style.font.name
    size = p.style.font.size
print (name, size)