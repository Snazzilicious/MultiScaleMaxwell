
import sympy as sp
from sympy import vector

C = sp.vector.CoordSys3D("C")


rho = sp.Function("rho")(C.x,C.y,C.z)

D1=sp.Function("D_1")(C.x,C.y,C.z)
D2=sp.Function("D_2")(C.x,C.y,C.z)
D3=sp.Function("D_3")(C.x,C.y,C.z)

D = D1*C.i + D2*C.j + D3*C.k

maxEQ1 = sp.vector.divergence(D) - rho
