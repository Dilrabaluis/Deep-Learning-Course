import numpy as np
x0=np.ones(10)
x1=[64.3,99.6,145.45,63.75,135.46,92.85,86.97,144.76,59.3,116.03]
x2=[2,3,4,2,3,4,2,4,1,3]
y=[62.55,82.42,132.62,73.31,131.05,86.57,85.49,127.44,55.25,104.84]
#（1）
X=np.stack((x0,x1,x2),1)
print("X=")
print(X)
print("=============分割线==============")
Y=np.array(y).reshape(10,1)
print("Y=")
print(Y)
print("=============分割线==============")
#（2）
# W=np.matmul(np.matmul(np.matmul(np.transpose(X),np.linalg.inv(X)),np.transpose(X)),Y)
X1=np.mat(X)
Y1=np.mat(Y)
W=np.dot(np.dot(np.dot(X1.T,X1).I,X1.T),Y)
print("W=")
print(W)

