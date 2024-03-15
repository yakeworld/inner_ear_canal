import json
import numpy as np

def getplane(p_nodes):
    import numpy as np
    point_num=len(p_nodes)
    x2=[k[0] for k in p_nodes]
    y2=[k[1] for k in p_nodes]
    z2=[k[2] for k in p_nodes]
    #创建系数矩阵A
    A=np.zeros((3,3))
    for i in range(0,point_num):
        A[0,0]=A[0,0]+x2[i]**2
        A[0,1]=A[0,1]+x2[i]*y2[i]
        A[0,2]=A[0,2]+x2[i]
        A[1,0]=A[0,1]
        A[1,1]=A[1,1]+y2[i]**2
        A[1,2]=A[1,2]+y2[i]
        A[2, 0] = A[0,2]
        A[2, 1] = A[1, 2]
        A[2, 2] = point_num
    b = np.zeros((3,1))
    for i in range(0,point_num):
        b[0,0]=b[0,0]+x2[i]*z2[i]
        b[1,0]=b[1,0]+y2[i]*z2[i]
        b[2,0]=b[2,0]+z2[i]
    #求解X
    A_inv=np.linalg.inv(A)
    X = np.dot(A_inv, b)
    #print('平面拟合结果为：z = %.3f * x + %.3f * y + %.3f'%(X[0,0],X[1,0],X[2,0]))

    A=X[0,0]
    B=X[1,0]
    C=-1
    D=X[2,0]
    
     
    return([A,B,C,D])
 


positions = []

# 读取 JSON 文件
with open('AC_MEM1.mrk.json', 'r') as file:
    data = json.load(file)

# 提取所有控制点的 position

for markup in data['markups']:
    for control_point in markup['controlPoints']:
        position = control_point['position']
        positions.append(position)

# 打印所有 position
for position in positions:
    print(position)
    

print(positions)



# 读取 JSON 文件
with open('AC_MEM2.mrk.json', 'r') as file:
    data = json.load(file)

# 提取所有控制点的 position

for markup in data['markups']:
    for control_point in markup['controlPoints']:
        position = control_point['position']
        positions.append(position)

# 打印所有 position
for position in positions:
    print(position)
    

print(positions)




#x2=[k[0] for k in positions]

A,B,C,D=getplane(positions)

zp=[A,B,C]
zp=zp/np.linalg.norm(zp)
print(np.round(zp,4))
print(np.round(np.arccos(zp)/np.pi*180,2))    
angle3=np.round(np.arccos(zp)/np.pi*180,2)
print('|',np.round(zp,4),'|',angle3[0],'|',angle3[1],'|',angle3[2],'|')

