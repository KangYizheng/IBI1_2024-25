import re
output_file=f"tata_genes.fa" # output file name
with open ("C:/Users/ASUS/Desktop/大一下学期/IBI1_2024-25/Practical7/Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa",'r') as infile, open (output_file,'w') as outfile:# open the input and output files
    current_gene_name = "" # variable to store the current gene name
    current_sequence = "" # variable to store the current sequence
    for line in infile: # read the input file line by line
        if re.search('^>', line): # check if the line is a header line
            # check if the previous sequence contains a TATA box
            if  re.search(r'TATA[AT]A[AT]',current_sequence):
                outfile.write(f">{current_gene_name}\n{current_sequence}\n")
            current_gene_name=re.search(r"gene:.*?\s",line) 
            if current_gene_name:
                    current_gene_name = current_gene_name[0] # Extract the gene name from the header line
                    current_gene_name = re.sub(r'gene:','',current_gene_name) # delete the gene: from the header line
            current_sequence = ""
            
        else:
            current_sequence += line # append the sequence to the current sequence
            current_sequence = re.sub(r'\n','',current_sequence) # remove new line characters from the sequence
    # check for the last gene in the file
    if re.search('TATA[AT]A[AT]',current_sequence):
       outfile.write(f"{current_gene_name}\n{current_sequence}\n") # Write the gene name and sequence to the output file

print(f"Genes with TATA box written to {outfile}")