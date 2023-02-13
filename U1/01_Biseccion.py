import math as ma 

def fnEcuacion(valor):
    return pow(valor,2) -2


x1 = 1
x2 = 2
xm = 0
Es = 0.001
Er = abs(x2-x1)
i = 1
it = round((ma.log(x2-x1) - ma.log(Es)) / ma.log(2))
print(it)

print("i    |     x1    |     x2    |      Er   |     xm    |" \
           "   f(x1)  |   f(xm)   | f(x1) * f(xm) | \n")
while Er>=Es:
    xm = (x1 + x2) / 2
    print('{:.0f}    | {:.4f}    | {:.4f}    | {:.4f}    | {:.4f}    | {:.4f}   | {:.3f}    | {:.3f}        |'.format (i,x1,x2,Er,xm,fnEcuacion(x1),fnEcuacion(xm),fnEcuacion(x1)*fnEcuacion(xm)))
    if fnEcuacion(x1) * fnEcuacion(x2) > 0:
        x2 = xm
    else:
        x1 = xm
    Er = abs(x2 - x1)
    i += 1
print(xm)
