import re
input_donor=input("Enter the type of recepter(GTAG,GCAG,ATAC) ")# input types of gene
input_receptor=input("Enter the type of recepter(GTAG,GCAG,ATAC) ")# input types of gene   
output_file=f"{input_donor}{input_receptor}_spliced_genes.fa"   
if f"{input_donor}{input_receptor}" not in ['GTAG','GCAG','ATAC']:
    print("Invalid input. Please enter GTAG, GCAG, or ATAC.")
with open ("C:/Users/ASUS/Desktop/第二学期/Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa",'r') as infile, open (output_file,'w') as outfile:
    current_gene_name = ""
    current_sequence = ""
    for line in infile:
        if re.search('^>', line):
            if  re.search(fr'{input_donor}.*TATA[AT]A[AT].*{input_receptor}',current_sequence):
                # Extract the sequence between the donor and receptor sites
                    tim1=re.findall(fr'{input_donor}.*{input_receptor}',current_sequence)
                # Combine the extracted sequences into a single string
                    tim1=''.join(tim1)
                    time=len(re.findall(r'TATA[AT]A[AT]',tim1))
                    current_sequence=re.findall(fr'{input_donor}.*TATA[AT]A[AT].*{input_receptor}',current_sequence)
                    current_sequence=''.join(current_sequence)
                    outfile.write(f">{current_gene_name} time={time}\n{current_sequence}\n")
            current_gene_name=re.search(r"gene:.*?\s",line) 
            if current_gene_name:
                    current_gene_name = current_gene_name[0]
                    current_gene_name = re.sub(r'gene:','',current_gene_name)
            current_sequence = ""
        else:
            current_sequence += line
            current_sequence = re.sub(r'\n','',current_sequence)
        # check for the last gene in the file
    if re.search(fr'{input_donor}.*TATA[AT]A[AT].*{input_receptor}',current_sequence):
        # Extract the sequence between the donor and receptor sites
            tim1=re.findall(fr'{input_donor}.*{input_receptor}',current_sequence)
            # Combine the extracted sequences into a single string
            tim1=''.join(tim1)
            time=len(re.findall(r'TATA[AT]A[AT]',tim1))
                # Write the gene name and sequence to the output file
            current_gene_name = re.sub(r'gene:','',current_gene_name)
            current_sequence=re.findall(fr'{input_donor}.*TATA[AT]A[AT].*{input_receptor})',current_sequence)
            current_sequence=''.join(current_sequence)
                # Write the gene name, time, and sequence to the output file
            outfile.write(f">{current_gene_name} time={time}\n{current_sequence}\n")

print(f"Genes with TATA box written to {outfile}")
