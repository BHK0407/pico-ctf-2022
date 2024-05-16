from sympy import *

M=Matrix([[0,1,0,0],[0,0,1,0],[0,0,0,1],[55692,-9549,301,21]])
P,D = M.diagonalize()
Pi=P**-1
print(f"M = {M}\nP*D*P^-1 = {P*D*Pi}\n")
L=Matrix([[1,0,0,0]])*P # pre-multiply by [1,0,0,0]
R=Pi*Matrix([[1],[2],[3],[4]]) #post-multiply by [1;2;3;4]
f=1/gcd(tuple(R)) # pull out the gcd
R=f*R
print(f"f(n) = {L} * {D}**n * {R} // {f}")
n=symbols("n")
print(f"f(n) = ({(L*D**n*R)[0]}) // {f}")
