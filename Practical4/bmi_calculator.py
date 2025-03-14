#input the weight and height of a person and calculates the BMI of the person
#calculate the BMI of a person
#print out the BMI of the person
#determine if the person is underweight, normal weight or obese


Weight=float(input("the weight of person the weight is in kg")) 
Height=float(input("the height of person in m"))
BMI= Weight/(Height**2) #Use the formula to calculate BMI, BMI is a measure of body fat based on height and weight asd
if BMI > 30: 
   print("your BMI:",str(BMI),"You are obese")
elif BMI < 18.5:
   print("your BMI:",str(BMI),"You are underweight")
else:
   print("your BMI:",str(BMI),"You have a normal weight")