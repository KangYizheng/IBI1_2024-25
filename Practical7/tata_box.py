import re
with open ("C:/Users/ASUS/Desktop/第二学期/Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa",'r') as infile, open ("C:/Users/ASUS/Desktop/第二学期/IBI1_2024-25/Practical7/tata_genes.fa",'w') as outfile:
    current_gene_name = ""
    current_sequence = ""
    for line in infile:
        if re.search('^>', line):
            if  current_sequence and re.search(r'TATA[AT]A[AT]',current_sequence):
                outfile.write(f"{current_gene_name}\n{current_sequence}\n")
            current_gene_name=re.search(r"gene:.*?\s",line) 
            if current_gene_name:
                    current_gene_name = current_gene_name[0]
                    current_gene_name = re.sub(r'gene:','',current_gene_name)
            current_sequence = ""
            
        else:
            current_sequence += line
        # check for the last gene in the file
    if re.search('TATA[AT]A[AT]',current_sequence):
       outfile.write(f"{current_gene_name}\n{current_sequence}\n")

print(f"Genes with TATA box written to {outfile}")