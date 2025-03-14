


a=15 #The time of walk to the	bus stop
b=75 #the time of bus journey
c=a+b #the total of time of taking bus
d=5 #the time walk to the car
e=90 #the time of driving
f=d+e #the total time of driving
if f > c:
   print("#driving is longer,taking bus is quicker")
elif  f < c:
   print("#taking bus is longer, driving is quicker")
else:
   print("#driving is equal to taking bus")
   # taking bus is quicker


X = True 
Y = False
W =X and Y
print("W:",W)

#truth table
#  X     | Y     | W
#  True  | True  | True
#  True  | False | False
#  False | False | False
#  False | True  | False
