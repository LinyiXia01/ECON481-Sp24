## Exercise 0
def github(): 
    """
    This function returns a link to my solutions on GitHub.
    """    
    return "https://github.com/LinyiXia01/ECON481-Sp24/blob/main/hw2.py"

github()


# Exercise 1 
import numpy as np

def simulate_data(seed: int) -> tuple:
    """
    This function returns 1000 simulated observtions.
    """
    rng = np.random.default_rng(seed=481)
    x = rng.normal(loc = 0, scale = 2, size = (1000,3))
    error = rng.standard_normal(1000)
    y = (5 + 3*x[:,0] + 2*x[:,1] + 6*x[:,2] + error).reshape((-1,1))

    return (y,x)

y, X = simulate_data(481)
print("Shape of y:", y.shape)
print("Shape of X:", X.shape)


# Exercise 2
from scipy import optimize

def estimate_mle(y: np.array, X: np.array) -> np.array:
    """
    This function is to estimate the MLE parameters for all the coefficients in the regression model.
    """
    def neg_ll(params,y,X):
        """
        This function calculates the negative log-likelihood value.
        """
        beta0, beta1, beta2, beta3 = params
        epsilon = y[:,0] - beta0 - beta1*X[:,0] - beta2*X[:,1] - beta3*X[:,2] 
        ll = -0.5 * np.sum(np.log(2 * np.pi) + epsilon**2)
        return -ll

    result = optimize.minimize(
                      fun=neg_ll,
                      x0=np.ones(4),
                      args=(y, X),
                      method='Nelder-Mead')

    beta_mle = np.array(result.x)

    return beta_mle

y, X = simulate_data(481)
coef = estimate_mle(y, X)
print(coef)


# Exercise 3
def estimate_ols(y: np.array, X: np.array) -> np.array:
    """
    This function is to estimate the OLS coefficients in the regression model.
    """
    def ols(params,y,X):
        """
        This function calculates the OLS value.
        """
        beta0, beta1, beta2, beta3 = params
        epsilon = y[:,0] - beta0 - beta1*X[:,0] - beta2*X[:,1] - beta3*X[:,2] 
        ols = np.sum(epsilon**2)
        return ols

    result = optimize.minimize(
                      fun=ols,
                      x0=np.ones(4),
                      args=(y, X),
                      method='Nelder-Mead')

    beta_ols = np.array(result.x)

    return beta_ols

y, X = simulate_data(481)
print(estimate_ols(y, X))

