def main():
    c = input("Enter your three letter sequence: ")
    print(translate_codon(c))
def translate_codon (cod):
    """Translates a codon into an amino acid using an internal dictionary with
    the standard genetic code."""
    #only returns single codon to amino acid translation. Should improve to RNA to protein
    #  sequence translation. I think it can be used with a loop to build a protein
    #  sequence AA by AA, or it should have an inbuilt loop to build the sequence.
    tc = {"GCT":"A", "GCC":"A", "GCA":"A", "GCG":"A" , "TGT":"C", "TGC":"C", "GAT":"D", 
        "GAC":"D", "GAA":"E", "GAG":"E", "TTT":"F", "TTC":"F", "GGT":"G", "GGC":"G", "GGA":"G", 
        "GGG":"G", "CAT":"H", "CAC":"H", "ATA":"I", "ATT":"I", "ATC":"I", "AAA":"K", 
        "AAG":"K", "TTA":"L", "TTG":"L", "CTT":"L", "CTC":"L", "CTA":"L", "CTG":"L", "ATG":"M", "AAT":"N",
        "AAC":"N", "CCT":"P", "CCC":"P", "CCA":"P", "CCG":"P", "CAA":"Q",
        "CAG":"Q", "CGT":"R", "CGC":"R", "CGA":"R", "CGG":"R", "AGA":"R",
        "AGG":"R", "TCT":"S", "TCC":"S", "TCA":"S", "TCG":"S", "AGT":"S",
        "AGC":"S", "ACT":"T", "ACC":"T", "ACA":"T", "ACG":"T", "GTT":"V",
        "GTC":"V", "GTA":"V", "GTG":"V", "TGG":"W", "TAT":"Y", "TAC":"Y",
        "TAA":"_", "TAG":"_"}
    if cod in tc : return tc [cod]
    else : print("Invalid codon")
main()