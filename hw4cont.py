#Package used: scipy.optimize.differential_evolution
#Code modified from: https://machinelearningmastery.com/differential-evolution-global-optimization-with-python/#:~:text=The%20Ackley%20function%20is%20an,%5D%2C%20which%20evaluates%20to%200.0.


# differential evolution global optimization for the ackley multimodal objective function
from scipy.optimize import differential_evolution
from numpy import exp
from numpy import sqrt
from numpy import sin
from numpy import e
from numpy import pi
 
# objective function
def objective(v):
 x, y = v
 # return abs(x+y)*(1+abs(sin(abs(x)*pi))+abs(sin(abs(y)*pi)))
 return abs(x+y)*(1+abs(sin(3*abs(x)*pi))+abs(sin(3*abs(y)*pi))) #for 1b
 
# define range for input
# define the bounds on the search
bounds = [[-60, 40], [-30, 70]]
# perform the differential evolution search
result = differential_evolution(objective, bounds, maxiter=60)
# summarize the result
print('Status : %s' % result['message'])
print('Total Evaluations: %d' % result['nfev'])
# evaluate solution
solution = result['x']
evaluation = objective(solution)
print('Solution: f(%s) = %.5f' % (solution, evaluation))