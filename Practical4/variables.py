


a=15 #The time of walk to the	bus	stop
b=75 #the time of bus journey
c=a+b #the total of time of bus
d=5 #the time walk to the car
e=90 #the time of driving
f=d+e #the total of time
if f > c:
   print("#driving is longer,bus is quicker")
elif  f < c:
   print("#bus is longer, driving is quicker")
else:
   print("#driving is equal to bus")
   # bus is quicker


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
