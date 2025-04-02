import re
input_gene=input("Enter the type of recepter(GTAG,GCAG,ATAC) ")
output_file=f"{input_gene}_spliced_genes.fa"
if input_gene not in ['GTAG','GCAG','ATAC']:
    print("Invalid input. Please enter GTAG, GCAG, or ATAC.")
with open ("C:/Users/ASUS/Desktop/第二学期/Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa",'r') as infile, open (output_file,'w') as outfile:
    current_gene_name = ""
    current_sequence = ""
    for line in infile:
        if re.search('^>', line):
            if  re.search(r'TATA[AT]A[AT]',current_sequence)and re.search(input_gene,current_sequence):
                time=len(re.findall(r'TATA[AT]A[AT]',current_sequence))
                current_sequence = re.sub(r'\n','',current_sequence)
                outfile.write(f">{current_gene_name} time={time}\n{current_sequence}\n")
            current_gene_name=re.search(r"gene:.*?\s",line) 
            if current_gene_name:
                    current_gene_name = current_gene_name[0]
                    current_gene_name = re.sub(r'gene:','',current_gene_name)
            current_sequence = ""
            
        else:
            current_sequence += line
        # check for the last gene in the file
    if re.search('TATA[AT]A[AT]',current_sequence):
       current_sequence = re.sub(r'\n','',current_sequence)
       outfile.write(f"{current_gene_name} time={time}\n{current_sequence}\n")

print(f"Genes with TATA box written to {outfile}")
