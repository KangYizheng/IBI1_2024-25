# import necessarylibraries
import numpy as np
import matplotlib.pyplot as plt
#define the basic variables
N=10000 #total population
S0=N-1 #initial susceptible
I0=1    #initial infected
R0=0   #initial recovered
beta=0.3 #infection rate
gamma=0.05 #recovery rate
S=[S0]
I=[I0]
R=[R0]
#1000 time points
t_steps=1000
for t in range(t_steps):
  #calculate the prabability of infection 
   p=beta*(I[-1]/N)
  #Susceptible people become infected
   new_infections=np.random.choice(range(2),S[-1],p=[1-p,p]).sum()
    #Infected people recover
   new_recoveries=np.random.choice(range(2),I[-1],p=[1-gamma,gamma]).sum()
   S.append(S[-1]-new_infections)
   I.append(I[-1]+new_infections-new_recoveries)
   R.append(R[-1]+new_recoveries)

plt.plot(range(t_steps+1),S,label='Susceptible') 
plt.plot(range(t_steps+1),I,label='Infected')
plt.plot(range(t_steps+1),R,label='Recovered')
plt.xlabel('Time')
plt.ylabel('Number of people')
plt.title('SIR model')
plt.legend()
plt.show()