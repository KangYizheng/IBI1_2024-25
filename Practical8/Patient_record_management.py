name=input("Enter the name of the patient: ")# patient name
age=int(input("Enter the age of the patient: "))# patient age
date_of_latest_admission=input("Enter the date of latest admission of the patient: ")# date of latest admission
medical_history=input("Enter the medical history of the patient: ") # medical history
# patient record management system
class patients:
       def __init__ (self,name,age,date_of_latest_admission,medical_history):
        self.name=name
        self.age=age
        self.date_of_latest_admission=date_of_latest_admission
        self.medical_history=medical_history
       def print_details_of(self):
           print(f'Patient Name: {self.name}, Age: {self.age}, Date of Latest Admission: {self.date_of_latest_admission}, Medical History: {self.medical_history}')
         
patient=patients(name,age,date_of_latest_admission,medical_history)
patient.print_details_of()
#example input: name=John, age=30, date_of_latest_admission=2023-10-01, medical_history=Diabetes
#example output: Patient Name: John, Age: 30, Date of Latest Admission: 2023-10-01, Medical History: Diabetes