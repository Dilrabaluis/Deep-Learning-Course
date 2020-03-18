import numpy as np
print("请输入一个1-100之间的数字：")
number=int(input())
arr = np.random.rand(1000)
arrresult = []
def getResult(arr,number,arrresult):
    m=0
    for i in range(0,1000):
        if (i%number) == 0:     
            m=m+1
            arrresult.append([m,i,arr[i]])
    return arrresult
lastresult=getResult(arr,number,arrresult)
for m in range(0,len(lastresult)):
    print(lastresult[m])