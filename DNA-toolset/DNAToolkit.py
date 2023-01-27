# DNA Toolkit file
import collections
from Structures import *


# Check the sequence to make sure it is a DNA string (doesn't contain any random other characters)
def validateSeq(dna_seq):
    tmpseq = dna_seq.upper()
    for nuc in tmpseq:
        if nuc not in Nucleotides:
            return False
    return tmpseq

def countNucFrequency(seq):
    tmpFreqDict = {"A": 0, "C": 0, "G": 0, "T": 0}
    for nuc in seq:
        tmpFreqDict[nuc] += 1
    return tmpFreqDict
    #The above code works fine, but can be optimized using the code below. You will need to import collections
    #return dict(collections.Counter(seq))
    #The above is creating a dictionary, and counting through a frequency of a string


# ==== Transcription function ====
def transcription(seq):
    """DNA -> RNA Transcription. Replacing Thymine with Uracil"""
    return seq.replace("T", "U")

def reverse_complement(seq):
    """Swapping adenine with thymine and guanine with cytosine. Can reverse string if needed"""
#    return ''.join([DNA_ReverseComplement[nuc] for nuc in seq])#[::-1] #<- This will reverse the sequence
#    comp = ""
#    for i in seq:
#        comp += DNA_ReverseComplement[i]
#    return comp[::-1] #<- this will reverse the sequence
# === pythonic solution ===
    mapping = str.maketrans('ATCG', 'TAGC')
    return seq.translate(mapping)[::-1]


# ==== GC-content calculation ====
def gc_content(seq):
    """GC content in a DNA/RNA sequence as % of total sequence"""
    return round((seq.count('C') + seq.count('G')) / len(seq) * 100)

def gc_content_subseq(seq, k = 20):
    """GC content in a DNA/RNA sub-sequence length k. k = 20 by default"""
    res = []
    for i in range(0, len(seq) - k + 1, k):
        subseq = seq[i:i + k]
        res.append(gc_content(subseq))
    return res
    #list = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    #res = []
    #for i in range(0, len(list) - 5 + 1, 5):
    #    subseq = list[i:i + 5]
    #    print(subseq)
    # Above will show you how the function works using a simple list








