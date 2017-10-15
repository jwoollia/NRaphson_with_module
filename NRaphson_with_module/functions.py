import sys

def fpower(x:float,c:float,n:float) :
    """ Calculates x**n - c """
    return x**n - c

def newtraph(c:float,x:float,n:float,xtol:float,iter:int,info:str,func) :
    """ Solves Newton-Raphson """
    xtol=abs(xtol)
    dx = sys.float_info.max
    if abs(c)<xtol*xtol : 
        x = 0. 
        iter = 0
        info = "within tolerance of root 0"
    else : 
        info = "OK"
        while dx>xtol :
            iter = iter + 1
            if x==0 : x = xtol
            xu = x+2.*xtol
            xl = x-2.*xtol
            fu = func(xu,c,n)
            fl = func(xl,c,n)
            fdash = (fu-fl)/(xu-xl)
            dx = func(x,c,n)/fdash
            x = x - dx
            dx=abs(dx)
            if iter>3 and dx>lastdx :
                info = "algorithm is diverging!"
                break
            lastdx=dx
    return [x,iter,info]