Weight=float(input("#the weight of person the weight is in kg")) 
Height=float(input("the height of person  in m"))
BMI= Weight/(Height**2)
if BMI >= 30: #BMI is a measure of body fat based on height and weight that
   print("your BMI:",str(BMI),"You are obese")
elif BMI <=18.5:
   print("your BMI:",str(BMI),"You are underweight")
else:
   print("your BMI:",str(BMI),"You have a normal weight")