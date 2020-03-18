from numpy import *
x=[64.3,99.6,145.45,63.75,135.46,92.85,86.97,144.76,59.3,116.03]
y=[62.44,82.42,132.62,73.31,131.05,86.57,85.49,127.44,55.25,104.84]
a=[1,2]
b=[1,2]
xave = mean(x)
yave = mean(y)
def getResult01(x,y):
    top=0
    bottom=0
    for i in range(0,len(x)):
        top+=(x[i]-xave)*(y[i]-yave)
        bottom+=(x[i]-xave)*(x[i]-xave)
    return top/bottom
print("W=",getResult01(x,y))
print("b=",yave-getResult01(x,y)*xave)