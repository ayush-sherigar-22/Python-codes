def analyze_dna_sequence(data):
    nucleotide_count={'A':0,'C':0,'G':0,'T':0}
    

    for nucleotide in data:
        if nucleotide in nucleotide_count:
            nucleotide_count[nucleotide]+=1
    return nucleotide_count


data= input("Enter DNA sequence (A/C/G/T) in capital :")
result=analyze_dna_sequence(data)
print(result)


