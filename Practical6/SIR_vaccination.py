# import necessary libraries
import numpy as np
import matplotlib.pyplot as plt

# Parameters
N = 10000  # total population
I0 = 1     # initial infected
R0 = 0     # initial recovered
beta = 0.3 # infection rate
gamma = 0.05 # recovery rate
t_steps = 1000 # number of time steps

vaccination_rates = [0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0]  # vaccination rates from 0 to 1

for rate in vaccination_rates:
    V0 = int(N * rate)
    S0 = max(N - I0 - V0, 0)  # Ensure susceptible is not negative

    S = [S0]
    I = [I0]
    R = [R0]

    for t in range(t_steps):
        if I[-1] == 0:
            S.extend([S[-1]] * (t_steps - t)) # extend susceptible with the last value
            I.extend([0] * (t_steps - t))
            R.extend([R[-1]] * (t_steps - t))
            break

        p_infect = beta * I[-1] / N  # probability of infection
        p_infect = min(max(p_infect, 0), 1) # ensure probability is between 0 and 1

        new_infections = np.random.binomial(max(S[-1], 0), p_infect) # susceptible people becoming infected
        new_recoveries = np.random.binomial(max(I[-1], 0), gamma) # infected people recovering

        S.append(S[-1] - new_infections) # update the number of susceptible people
        I.append(I[-1] + new_infections - new_recoveries) # update the number of infected people
        R.append(R[-1] + new_recoveries) # update the number of recovered people

    plt.plot(range(t_steps + 1), I, label=f'{int(rate * 100)}%')

# Plotting
plt.xlabel('Time')
plt.ylabel('Number of Infected People')
plt.title('SIR Model with Different Vaccination Rates')
plt.legend(title='Vaccination Rate')
plt.tight_layout()
plt.show()
