import re
#File paths
human=r"C:/Users/ASUS/Desktop/大一下学期/IBI1_2024-25/Practical13/human.fasta"
mouse=r"C:/Users/ASUS/Desktop/大一下学期/IBI1_2024-25/Practical13/mouse.fasta"
random=r"C:/Users/ASUS/Desktop/大一下学期/IBI1_2024-25/Practical13/Random.fasta"
blosum62=r"C:/Users/ASUS/Desktop/大一下学期/IBI1_2024-25/Practical13/BLOSUM62.txt"
def read_file(file_path):# get the sequence from the file
    sequence = "" #initialize an empty string
    with open(file_path,"r")as file: #open the file
        for line in file:
            if not re.search(r"^>", line):
                sequence += line.strip() #Get the sequence line and remove the newline character
    return sequence
def load_blosum62(filepath): #load the BLOSUM62 matrix from the file
    with open(filepath, 'r') as file:
        matrix = {} #initialize an empty dictionary
        # remove empty lines and comments
        lines = [line.strip() for line in file if line.strip() and not line.startswith('#')]
        header = lines[0].split() # get the header
        for line in lines[1:]:
            parts = line.split()# split the line into parts
            row_aa = parts[0] # get the row amino acid
            # get the scores for the row amino acid
            scores = list(map(int, parts[1:]))
            # create a dictionary with the amino acids as keys and the scores as values
            for col_aa, score in zip(header, scores):
                matrix[(row_aa, col_aa)] = score
    return matrix
     
def similiarity(seq1, seq2): #calculate the similarity between two sequences
    if len(seq1) != len(seq2):# check if the two sequences are of the same length
        raise ValueError("Sequences must be of the same length")
    similiarity_count = 0 #initialize the similarity count
    scores = 0 #initialize the score
    for i in range(len(seq1)):
        scores += matrix[(seq1[i], seq2[i])] # sum the score of the two sequences
        if seq1[i] == seq2[i]:
            similiarity_count += 1 #sum the number of identical amino acids
    # calculate the similarity
    similiarity = similiarity_count / len(seq1)
    print(f"Similarity: {similiarity*100:.2f}%")
    print(f"Score: {scores}")

# get the matrix
matrix=load_blosum62(blosum62)
# get the length of the sequence
length_SOD2 = len(read_file(human))
# get the sequence
sequence_h= read_file(human)
sequence_m= read_file(mouse)
sequence_r= read_file(random)
# get the similarity and score
similarity_hm = similiarity(sequence_h, sequence_m)# similarity between human and mouse
similarity_hr = similiarity(sequence_h, sequence_r)# similarity between human and random
similarity_mr = similiarity(sequence_m, sequence_r)# similarity between mouse and random
print(f"Length of SOD2: {length_SOD2}")




            
    
