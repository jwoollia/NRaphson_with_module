import numpy as np
from io import StringIO
import numpy as np
from io import StringIO
import functions as jf
print("Default tolerance is 1.0e-6 ")

with open('nrtest.txt','r') as fn :
    sol = []
    cyc = []
    for line in fn :
        c,x,n = np.loadtxt(StringIO(line), delimiter=',', comments='#', usecols=(1,2,4))
        xtol,iter,info = 1.e-6, 0, 'in'
        [x,iter,info] = jf.newtraph(c,x,n,xtol,iter,info,jf.fpower)
        print ("Target %6.2f, %4.1f-root is %10.6f, iteration %3d ... %s " % (c,n,x,iter,info))
        sol.append(x)
        cyc.append(iter)

print (sol)
print (cyc)
sol = np.array(sol,float)
cyc = np.array(cyc,int)
print (sol.shape,cyc.shape,2*cyc.shape[0])
print (np.exp(sol))
print (np.dot(sol,cyc))