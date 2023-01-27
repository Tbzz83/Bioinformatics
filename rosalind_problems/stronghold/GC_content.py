

def readFile(filePath):
    with open (filePath, 'r') as f:
        return [l.strip() for l in f.readlines()]
        #.strip removes leading and trailing whitespaces


def gc_content(seq):
    """GC content in a DNA/RNA sequence as % of total sequence"""
    return round((seq.count('C') + seq.count('G')) / len(seq) * 100, 3)


# === Read data from file (FASTA formatted)

# Storing file Contents in a list
FASTAFile = readFile(r"C:\Users\Tobi\Downloads\rosalind_gc.txt")

# Dictionary for Labels + data
FASTADict = {}

# String for holding the current label
FASTALabel = ""



# Converting FASTA/List file data into a dictionary
# === Clean/Prep data
for line in FASTAFile:
    if '>' in line:
        FASTALabel = line
        FASTADict[FASTALabel] = ""
    else:
        FASTADict[FASTALabel] += line

print(f'Here is the dictionary:\n{FASTADict}')

# Creating results dictionary
# === Format data (store in convenient way)
# === run needed operations
RESULTDict = {key: gc_content(value) for key, value in FASTADict.items()}

print(f'This is the results dictionary:\n{RESULTDict}')

# Looking for max values
MaxGCKey = max(RESULTDict, key = RESULTDict.get)
# See misc\max_fn_dict.py for how this loop works


# === Collect results
print(f'{MaxGCKey[1:]}\n{RESULTDict[MaxGCKey]}')