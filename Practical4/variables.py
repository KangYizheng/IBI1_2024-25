from re import X


a=15 #The time of walk to the	bus	stop
b=75 #the time of bus journey
c=a+b #the total of time of bus
d=5 #the time walk to the car
e=90 #the time of driving
f=d+e #the total of time
if f >= c:
   print("#driving is longer")
elif  f <= c:
   print("#bus is longer")
elif f == c:
   print("#driving is equal to bus")
   # bus is quicker


X == True 
Y == Flase
W ==X and Y

#truth table
#  X | Y | W
#  T | T | T
#  T | F | F
#  F | F | F
#  F | T | F