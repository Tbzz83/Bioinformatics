DNA_ReverseComplement = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}


def reverse_complement(seq):
    """Swapping adenine with thymine and guanine with cytosine. Can reverse string if needed"""
    return ''.join([DNA_ReverseComplement[nuc] for nuc in seq])[::-1] #<- This will reverse the sequence
#    comp = ""
#    for i in seq:
#        comp += DNA_ReverseComplement[i]
#    return comp[::-1] #<- this will reverse the sequence

print(reverse_complement("ATCAGACGGGGAGGCTACGTGGTTATTAGTCCCTCGCTTCGAACGAATGAAGTTCGGATAGGGCGGTCAGTTGCACTGCGCATTGCAATTGCCCGAGCATCCTCTAAACCCTGTCTAGGGCGCAGATGCTGTTAGGATACAACACTAACCCGCGGACACCCCGCGAGAATAAGTTTGCTAAGACCGATCACGCGTAGCTCTGCGCATTGGGCACCATTTACGAGGACGGGCGACTTCAATCTCACCCGTCCCCCAATACCTTCTGTAACATTGTAATCGCAATATACCAGAGACGGATGGACTGGATAATAGGAGAGTGTGGAGGCGGTCCATCTGTGAACTAGAGTAGTCGGTCGGTGCTTTAGCTGCCCCAAGAGGGGCACGGTCGATGTTCTAGCAATGGCTTAATAATACACGATTGGTCGGTTGGCGCCAGGCAGTCTCGACATCAGAAAATTAATGGCTCGTCCGAAAGGCTCCGTCGAGGGCAAAATGCTTCAAACGGGCGAACCGAAGTGTATAGGGACGCGAGGTCGTAACTTACTATCAACCATCGGTATGCAAGGATGAACTTAAAAGTAAGCGTATAAGGAACCACAAGTGTTTCTCGTACTCCATTCGATCCCACGGTAAAAAGAACCAATACGACCAACCTACTCCCGCACATAAGCTTTACGCTCAGATTCATCCAGGAGAAAGGCATAATACAGCTCCTTTCCGAAGATCCAAGGTCACATCTGAAGCTGTGCCGGGCACCCCGGCATAGATGCGGCGAAGTACAATTCGTACTAAGGCACAGCTAGACCCAAGTTGATCGAGATCACGTCTACAAATTACCGGTGTCCATGCGGCTGACTAATAGAACG"))