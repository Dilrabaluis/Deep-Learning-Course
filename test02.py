print("请输入a、b、c三个整数：")
a=int(input())
b=int(input())
c=int(input())
def getResult(a,b,c):
    if (b*b-4*a*c)<0:
        return "无实根"
    else:
        p=pow(b*b-4*a*c,0.5)
        m1=-b+p
        m2=-b-p
        x1=m1/(2*a)
        x2=m2/(2*a)
        return x1,x2
print(getResult(a,b,c))