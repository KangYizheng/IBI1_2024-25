import re
input_donor=input("Enter the type of recepter(GTAG,GCAG,ATAC) ")# input types of donor
input_receptor=input("Enter the type of recepter(GTAG,GCAG,ATAC) ")# input types of receptor
# input the type of donor and receptor   
output_file=f"{input_donor}{input_receptor}_spliced_genes.fa"   
if f"{input_donor}{input_receptor}" not in ['GTAG','GCAG','ATAC']:# check if the input is valid
    print("Invalid input. Please enter GTAG, GCAG, or ATAC.")
with open ("C:/Users/ASUS/Desktop/第二学期/Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa",'r') as infile, open (output_file,'w') as outfile:# open the input and output files
    current_gene_name = ""
    current_sequence = ""
    for line in infile:       # read the input file line by line
        # check if the line is a header line                            
        if re.search('^>', line):
            if  re.search(fr'TATA[AT]A[AT]',current_sequence) and re.search(fr'{input_donor}.*{input_receptor}',current_sequence):              
                    time=len(re.findall(r'TATA[AT]A[AT]',current_sequence))     #count the number of TATA boxes in the sequence 
                    outfile.write(f">{current_gene_name} time={time}\n{current_sequence}\n") # write the gene name, time, and sequence to the output file
            # Extract the gene name from the header line
            current_gene_name=re.search(r"gene:.*?\s",line) 
            if current_gene_name:# delete the gene: from the header line
                    current_gene_name = current_gene_name[0]
                    current_gene_name = re.sub(r'gene:','',current_gene_name)
            current_sequence = ""
        else:
            current_sequence += line # append the sequence to the current sequence
            # Remove new line characters from the sequence
            current_sequence = re.sub(r'\n','',current_sequence)
        # check for the last gene in the file
    if re.search(fr'{input_donor}.*TATA[AT]A[AT].*{input_receptor}',current_sequence):
        # Extract the sequence between the donor and receptor sites
            time=len(re.findall(r'TATA[AT]A[AT]',current_sequence))
                # Write the gene name and sequence to the output file
            current_gene_name = re.sub(r'gene:','',current_gene_name)
                # Write the gene name, time, and sequence to the output file
            outfile.write(f">{current_gene_name} time={time}\n{current_sequence}\n")

print(f"Genes with TATA box written to {outfile}")
