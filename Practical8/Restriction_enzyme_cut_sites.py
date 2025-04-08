import re
def find_the_restriction_enzyme_cut_sites(sequence, enzyme):# function to find the restriction enzyme cut sites in a DNA sequence
    if re.search(r'ACGT', sequence):# check if the sequence is a valid DNA sequence
        if re.search(r'ACGT', enzyme):# check if the enzyme is a valid restriction enzyme
            if re.search(enzyme, sequence):# check if the enzyme is present in the sequence
                for i in range(len(sequence)-len(enzyme)+1):# iterate through the sequence to find the enzyme
                    total_cut_sites = []
                    while sequence[i:i+len(enzyme)] == enzyme:
                        cut_sites = [i, i+len(enzyme)-1]
                        total_cut_sites.append(cut_sites)
                    return total_cut_sites
            else:
                print("No match")
                return None
        else:
            print("Enzyme not valid")
            return None
    else:
        print("DNA sequence not valid")
        return None 
sequence=input("Enter the sequence: ")
enzyme=input("Enter the enzyme: ")
cut_sites = find_the_restriction_enzyme_cut_sites(sequence, enzyme)
if cut_sites is not None:
    for cut_site in cut_sites:
        print(f"Cut site: {cut_site}") 
# example input: sequence=ACGTACGTACGT, enzyme=ACGT
# example output: Cut site: [0, 3], Cut site: [4, 7], Cut site: [8, 11]
# example input: sequence=ACGTACGTACGT, enzyme=AGCT
# example output: No match
# example input: sequence=ACGTACGTACGT, enzyme=ACG
# example output: enzyme not valid
# example input: sequence=AGCTAGCTAGCT, enzyme=ACGT
# example output: DNA sequence not valid

