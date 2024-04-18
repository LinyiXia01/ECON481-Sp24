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

rng = np.random.default_rng(seed=1)

X = rng.normal(scale=np.sqrt(2), size = (1000, 3))
y = 5 + X @ np.array([3.,2.,6.]) + rng.standard_normal(1000)


def test_simulation_shapes():
    assert simulate_data()[0].shape in [(1000,), (1000,1)]
    assert simulate_data()[1].shape == (1000,3)

def test_simulation_means():
    assert np.allclose(np.mean(simulate_data()[0]), 5., atol=3*np.sqrt(((9+4+36)*2+1)/1000), rtol=0)
    assert np.allclose(np.mean(simulate_data()[1]), 0., atol=3*np.sqrt(2/3000), rtol=0)

def test_simulation_vars():
    assert np.allclose(np.var(simulate_data()[0]), (9+4+36)*2+1, rtol=.1, atol=0)

def test_mle_coef_shape():
    assert estimate_mle(y,X).shape in [(4,), (4,1)]

def test_mle_coef_vals():
    assert np.allclose(estimate_mle(y,X).flatten(), np.array([5., 3., 2., 6.]), atol=0, rtol=.25)

def test_mle_coef_vals_unseen():
    beta = np.array([6., 5, -5, 2])
    y_new = beta[0] + X @ beta[1:] + rng.normal(size=1000,scale=3)
    assert np.allclose(estimate_mle(y_new, X).flatten(), beta, atol=0, rtol=.25)

def test_mle_coef_vals_unseen_2():
    beta = np.array([1., -2, -1., 2])
    y_new = beta[0] + X @ beta[1:] + rng.normal(size=1000,scale=3)
    assert np.allclose(estimate_mle(y_new, X).flatten(), beta, atol=0, rtol=.25)

def test_ols_coef_shape():
    assert estimate_ols(y,X).shape in [(4,), (4,1)]

def test_ols_coef_vals():
    assert np.allclose(estimate_ols(y,X).flatten(), np.array([5., 3., 2., 6.]), atol=0, rtol=.25)

def test_ols_coef_vals_unseen():
    beta = np.array([6., 5, -5, 2])
    y_new = beta[0] + X @ beta[1:] + rng.normal(size=1000,scale=3)
    assert np.allclose(estimate_ols(y_new, X).flatten(), beta, atol=0, rtol=.25)

def test_ols_coef_vals_unseen_2():
    beta = np.array([1., -2, -1., 2])
    y_new = beta[0] + X @ beta[1:] + rng.normal(size=1000,scale=3)
    assert np.allclose(estimate_ols(y_new, X).flatten(), beta, atol=0, rtol=.25)