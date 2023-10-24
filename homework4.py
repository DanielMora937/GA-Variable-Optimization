#Package used: scipy.optimize.differential_evolution
#Code modified from: https://machinelearningmastery.com/differential-evolution-global-optimization-with-python/#:~:text=The%20Ackley%20function%20is%20an,%5D%2C%20which%20evaluates%20to%200.0.


# differential evolution global optimization for the ackley multimodal objective function
from scipy.optimize import differential_evolution
from numpy import exp
from numpy import sqrt
from numpy import cos
from numpy import e
from numpy import pi
 
# objective function
def objective(v):
 x, y = v
 return -10 * exp(-0.18 * sqrt((1/30) * (x**2 + y**2))) - exp((1/30) * (cos(2 * pi * x) + cos(2 * pi * y))) + e + 10
 
# define range for input
r_min, r_max = -30.0, 30.0
# define the bounds on the search
bounds = [[r_min, r_max], [r_min, r_max]]
# perform the differential evolution search
result = differential_evolution(objective, bounds, strategy='best2bin', recombination=0.99,)
# summarize the result
print('Status : %s' % result['message'])
print('Total Evaluations: %d' % result['nfev'])
# evaluate solution
solution = result['x']
evaluation = objective(solution)
print('Solution: f(%s) = %.5f' % (solution, evaluation))