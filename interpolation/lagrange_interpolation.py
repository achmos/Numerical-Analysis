from numpy import poly1d

"""
This Modules implements the Lagrange Interpolating polynomial.
"""

"create a new list of x values without the" 
"x value located at position [index] in the array"
def xvals_not_i(x_values,index):
    new_x_values = []
    
    for i in range(len(x_values)):
        if i == index:
            continue
        new_x_values.extend([x_values[i]])
        
    return new_x_values

"Create a polynomial with roots that are all Xs except X_index"
def BasisNumerator(x_values, index):
    new_x_list = xvals_not_i(x_values,index)
    Basis_Numerator = poly1d(new_x_list,True)
    return Basis_Numerator

"Create a Lagrange Basis polynomial of degree n-1 for x_i for lagrange interpolation"
def LangrangeBasisPoly(x_valus, index):
    Numerator = BasisNumerator(x_valus, index)
    Denominator = Numerator(x_valus[index])
    BasisPoly = Numerator / Denominator
    return BasisPoly

"Create a lagrange interpolating polynomial"
def lagrangePoly(X_values,Y_values):
    LagPoly = 0 #initialize
    
    #build interpolating polynomial  
    for i in range(len(X_values)):
        LagPoly = LagPoly + Y_values[i] * LangrangeBasisPoly(X_values, i)
         
    return LagPoly

"Create a polynomial whose roots are the values in the array x_values"
def pi_ofX(x_values):
    pi_poly = 1
    for x in x_values:
        pi_poly = pi_poly * poly1d(x,True)
    return pi_poly