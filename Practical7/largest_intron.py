seq="ATGCAAGTGGTGTGTCTGTTCTGAGAGGGCCTAA"
for i in range(len(seq)):
    if seq[i:i+2] == "GT":
       for j in range(i+2, len(seq)):
           if seq[j:j+2] == "AG":
               length = j - i + 2
               max_length = 0
               if length > max_length:
                    max_length = length
print(max_length)
                    
                   

               