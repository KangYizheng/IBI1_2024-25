# pseudocode:
# Define sum as zero;
# Repeat:(define a number i that increase 1 after every loop)
#   add the i into the sum;
#   print the value of sum;


sum=0 # sum is the total of dots 
for j in range(1,11): # j is the triangle number
    sum += j
    print("sum:",sum)
#This can be written as an arithmetic sequence, where the number of points in the first triangle plus the number
# of points in the second triangle is the total number of triangles.