import numpy as np
import matplotlib.pyplot as plt
# identify the basic variables
beta = 0.3 
gamma = 0.1  
num_time_points = 100  
# the initial population
population = np.zeros((100, 100))
# set the initial infection point
outbreak = np.random.choice(range(100), 2)
population[outbreak[0], outbreak[1]] = 1
for t in range(num_time_points):
    # find the infected individuals
    infected_points = np.where(population == 1)

    # infection spread
    for i,j in zip(infected_points[0], infected_points[1]):
        # infect the surrounding individuals
        for x in range(max(0,i-1),min(i+2,100)):
            for y in range(max(0,j-1), min(100,j+2)):
                # check if the point is within the population
                if (x,y) != (i,j) and population[x, y] == 0:
                        # infect the individual
                        population[x, y] = np.random.choice(range(2),1, p=[1-beta, beta])
    # infected individuals recover
    recovered_points = np.where((population == 1) & (np.random.random(population.shape) < gamma))
    population[recovered_points] = 2

    plt.figure(figsize=(6, 4), dpi=150)
    plt.imshow(population, cmap='viridis', interpolation='nearest')
    plt.title(f"Time point {t}")
    plt.show()