seq="ATGCAAGTGGTGTGTCTGTTCTGAGAGGGCCTAA" 
for i in range(len(seq)): # iterate through the sequence
    if seq[i:i+2] == "GT": # check for the start codon
       for j in range(i+2, len(seq)): 
           if seq[j:j+2] == "AG": # check for the stop codon
               length = j - i + 2  # calculate the length of the intron
               max_length = 0
               if length > max_length:# check if the length is greater than the current maximum length
                    max_length = length # update the maximum length
print(max_length)
                    
                   

               