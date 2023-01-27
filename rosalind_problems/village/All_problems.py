
input = "dFe7tVc6A4b76m11CImIY5cNf6vObF5F1PPwm7tpWuQvdtxdvRp9pRHEschrichtiusuwZeyimhQVf7tWL4cn9f6qZvHhJLI1ZHlVHuQN433YxbpGFCDbCTRzfeILfxm5v4ttmSLnxx0aGAHUTwNgsdAwCE45zQlvanellusFIXGGpxHvcDpu52G9AvWg0KGjq6u2."

a = 55
b = 66
c = 160
d = 167

#def slicer (input, a, b, c, d):
#    result = ""
#    for i in input[a:b+1]:
#        result += i

#    result += " "
#    for i in input[c:d+1]:
#        result += i
#    return(result)


#print(slicer(input,a,b,c,d))


#or

f'{input[a:b+1]} {input[c:d+1]}'

# ==== Conditions and Loops ====

# Given: Two positive integers a and b (a<b<10000).
#
# Return: The sum of all odd integers from a through b, inclusively.

a = 4795
b = 9302
#result = 0

#for x in range(a,b+1):
#    if  x % 2 != 0:
#       result += x

#or

result = sum([x for x in range(a, b +1) if x % 2 != 0])

#print(result)


# ==== Reading and Writing ====

outputFile = []

with open("Sample_reading_writing.txt" , "r") as f:
    outputFile = [line for pos, line in enumerate(f.readlines()) if pos % 2 != 0]



with open('out.txt', 'w') as f:
    f.write(''.join([line for line in outputFile]))

# The readlines() method returns a list containing each line in the file as a list item.

# ==== Dictionaries ====

txtStr = "When I find myself in times of trouble Mother Mary comes to me Speaking words of wisdom let it be And in my hour of darkness she is standing right in front of me Speaking words of wisdom let it be Let it be let it be let it be let it be Whisper words of wisdom let it be And when the broken hearted people living in the world agree There will be an answer let it be For though they may be parted there is still a chance that they will see There will be an answer let it be Let it be let it be let it be let it be There will be an answer let it be Let it be let it be let it be let it be Whisper words of wisdom let it be Let it be let it be let it be let it be Whisper words of wisdom let it be And when the night is cloudy there is still a light that shines on me Shine until tomorrow let it be I wake up to the sound of music Mother Mary comes to me Speaking words of wisdom let it be Let it be let it be let it be yeah let it be There will be an answer let it be Let it be let it be let it be yeah let it be Whisper words of wisdom let it be"

# Generic approach
wordCountDict = {}

#for word in txtStr.split(" "):
#    if word in wordCountDict:
#        wordCountDict[word] += 1
#    else:
#        wordCountDict[word] = 1



# OR

from collections import Counter


wordCountDict = Counter(txtStr.split(' '))

#Printing wordCountDict gives you a dict with key values for frequency of all items
#print(wordCountDict)

for key, value in wordCountDict.items():
    print(key, value)






