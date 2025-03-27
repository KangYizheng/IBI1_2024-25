# import necessarylibraries
import numpy as np
import matplotlib.pyplot as plt

vaccination_rates=[0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1]#define the vaccination rates

  
for rate in vaccination_rates:
#define the basic variables
    N=10000
    V0=int(N*rate)#Vaccinated people
    I0=1    #initial infected
    S0=N-I0-V0#intial susceptible
    R0=0   #initial recovered
    beta=0.3 #infection rate
    gamma=0.05 #recovery rate
  #define the lists to store the number of people in each category
    S=[S0]
    I=[I0]
    R=[R0]
    V=[V0]
 
  #define the time steps
    t_steps=1000
    #When the vaccination rate is 100%, the number of vaccinated people is equal to the total population, so the number of infected people is 0.
    #but the value of (N-V0) can't be 0, so we need to divide the situation to discuss.
    if rate == 1:
        I = [0] * (t_steps + 1) 
    else:
        for t in range(t_steps):
            # calculate the prabability of infection
            p = beta * (I[-1] / (N - V0))
            # infection
            new_infections = np.random.choice(range(2), S[-1], p=[1 - p, p]).sum()
            # recovery
            new_recoveries = np.random.choice(range(2), I[-1], p=[1 - gamma, gamma]).sum()
            S.append(S[-1] - new_infections)
            I.append(I[-1] + new_infections - new_recoveries)
            R.append(R[-1] + new_recoveries)
            V.append(V0)
    plt.plot(range(t_steps + 1), I, label=f'{rate*100}%')

plt.xlabel('Time')
plt.ylabel('Number of people')
plt.title('SIR model with different vaccination rates')
plt.legend()
plt.show()

