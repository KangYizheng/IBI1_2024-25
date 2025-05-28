import re
seq="ATGCAAGTGGTGTGTCTGTTCTGAGAGGGCCTAA" 
max_length = 0 # define the maximum length of the intron
if not re.search("GT", seq): # check if the sequence contains splice-donor site
    print("splice-donor site not found")
if not re.search("AG", seq): # check if the sequence contains splice-acceptor site
    print("splice-recepter site not found")
if re.search("GT.*AG", seq): # check if the sequence contains a splice site
    for i in range(len(seq)): # iterate through the sequence
        if seq[i:i+2] == "GT": # check for the start codon
            for j in range(i+2, len(seq)): # iterate through the sequence
                if seq[j:j+2] == "AG": # check for the stop codon
                    length = j - i + 2  # calculate the length of the intron
                    if length > max_length: # check if the length is greater than the current maximum length
                        max_length = length # update the maximum length
                        splice_sequence = seq[i:j+2] # store the splice sequence
print(f"the longest intron is {max_length} nucleotides long and the sequence is {splice_sequence}") # print the result
                    
                   

               