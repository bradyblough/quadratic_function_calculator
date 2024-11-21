from sympy import Symbol, plot, sqrt

def graph(a,b,c):
    x = Symbol("x")
    return plot(a*x**2+b*x+c)

def roots(a,b,c):
    d = sqrt(b*b-4*a*c) # d = discriminant because I thought it was confusing to add a word to an expression 
    x1 = (-b + d)/(2*a)
    x2 = (-b - d)/(2*a)
    return x1, x2

def main():
    print("Welcome to the Quadratic Function Calculator! ")
    print("Standard Form is a * x^2 + b * x + c")
    a = float(input ("Enter the a component: "))
    b = float(input ("Enter the b component: "))
    c = float(input ("Enter the c component: "))
    print("The roots of this function are", roots(a,b,c))
    graph(a,b,c)

main()