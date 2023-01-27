# DNA Toolset/Code testing file
from DNAToolkit import *
from Utilities import colored
import random

rndDNAStr = "".join([random.choice(Nucleotides) for nuc in range(50)])

DNAStr = validateSeq(rndDNAStr)


print(f'\nSequence: {colored(DNAStr)}\n')
print(f'[1] + Sequence length: {len(DNAStr)}\n')
print(colored(f'[2] + Nucleotide frequency: {countNucFrequency(DNAStr)}\n'))
print(f'[3] + DNA -> RNA transcription: {transcription(colored(DNAStr))}\n')
print(f"[4] + DNA String + Reverse complement:\n\n5' {colored(DNAStr)} 3'")
print(f"   {''.join(['|' for c in range(len(DNAStr))])}")
print(f"3' {colored(reverse_complement(DNAStr))} 5'\n")

print(f'[5] + GC content: {gc_content(DNAStr)}%\n')

print(f'[6] + GC content (%) in subsection k = 5: {gc_content_subseq(DNAStr, k=5)}\n')


