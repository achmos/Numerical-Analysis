from numpy import poly1d
from lagrange_interpolation import langrange_basis_poly

"""
Hermite interpolations as defined using lagrange interpolating
basis polynomials to define our hermite interpolating polynomial
"""

# create a hermite basis polynomial for the y_values to multiply against
def hermite_basis_poly(x_values, index):
    lag_basis = langrange_basis_poly(x_values, index) 
    value = lag_basis.deriv()(x_values[index])
    poly = (1 - 2 * value  * poly1d(x_values[index],True) )
    herm_basis = (lag_basis**2) * poly 
    
    return herm_basis 

# create a basis polynomial to multiply against the y values of the derivative
def hermite_basis_deriv_poly(x_values, index):
    lag_basis = langrange_basis_poly(x_values, index)
    poly = poly1d(x_values[index],True)
    herm_basis_deriv = (lag_basis**2) * poly
     
    return herm_basis_deriv

# Create a Hermite Interpolating polynomial
def hermite_poly(x_values, y_values, y_primes):
    herm_poly = 0 
    
    for i in range(len(x_values)):
        herm_poly += y_values[i]*hermite_basis_poly(x_values, i)
        
    for i in range(len(x_values)):
        herm_poly += y_primes[i] * hermite_basis_deriv_poly(x_values, i)
          
    return herm_poly