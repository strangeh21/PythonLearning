# Deoxyribonucleic acid (DNA) is a chemical found in the nucleus of cells and carries the "instructions" for the development and functioning of living organisms.
#
# If you want to know more: http://en.wikipedia.org/wiki/DNA
#
# In DNA strings, symbols "A" and "T" are complements of each other, as "C" and "G". You function receives one side of the DNA (string, except for Haskell); you need to return the other complementary side. DNA strand is never empty or there is no DNA at all (again, except for Haskell).
#
# More similar exercise are found here: http://rosalind.info/problems/list-view/ (source)
#
# Example: (input --> output)
#
# "ATTGC" --> "TAACG"
# "GTAT" --> "CATA"
#
# dnaStrand []        `shouldBe` []
# dnaStrand [A,T,G,C] `shouldBe` [T,A,C,G]
# dnaStrand [G,T,A,T] `shouldBe` [C,A,T,A]
# dnaStrand [A,A,A,A] `shouldBe` [T,T,T,T]

def DNA_strand(dna):
    swapped_dna = ""
    for n in range(len(dna)):
        if dna[n] == "A":
            swapped_dna += "T"
        elif dna[n] == "T":
            swapped_dna += "A"
        elif dna[n] == "G":
            swapped_dna += "C"
        elif dna[n] == "C":
            swapped_dna += "G"
        else:
            pass
    return swapped_dna

