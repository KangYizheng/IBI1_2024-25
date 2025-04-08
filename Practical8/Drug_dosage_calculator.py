# Drug dosage calculator
# This program calculates the volume of a drug required for a patient based on their weight and the strength of the drug.
def calculate_dosage(weight,strength):
    if weight<10 or weight>100:   # check if weight is in the range of 10 to 100 kg
        print("Weight is out of range,there is a valuable error")
    normal_strength={120,250}
    if strength not in normal_strength:  # check if strength is in the set of normal strengths
        print("Strength is out of range,there is a valuable error")
    if weight<10 or weight>100 or strength not in normal_strength: 
        return None
    required_dosage=weight*15    # calculate the required dosage in mg
    volume=(required_dosage/strength)*5    # calculate the volume in ml
    return volume
weight=int(input("Enter the weight of the patient in kg: "))
strength=int(input("Enter the strength of the drug in mg/ml: "))
volume=calculate_dosage(weight,strength)
if volume :
    print(f"The required volume of the drug is {volume} ml")
# example input: weight=70, strength=120
# example output: The required volume of the drug is 43.75 ml

    