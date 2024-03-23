import os
import json
import re

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
 
 
 
 

def get_json_data(dir_path):
   data_dict = {}
   for filename in os.listdir(dir_path):
       if filename.endswith('.mrk.json'):
           file_path = os.path.join(dir_path, filename)
           with open(file_path, 'r', 	encoding='utf-8') as f:
               data = json.load(f)
               positions=get_position(data)
               base_name = '.'.join(filename.split('.')[:-2])
               #base_name = os.path.splitext(os.path.basename(filename))[0]
               base_name = re.sub(r'\d+','', base_name) # 删除数字后缀
               #print('now',base_name)
               if base_name in data_dict:
                   data_dict[base_name]=data_dict[base_name] + positions
               else:
                   data_dict[base_name] = positions
   return data_dict


def get_position(data):
        positions = []
        for markup in data['markups']:
            for control_point in markup['controlPoints']:
                position = control_point['position']
                positions.append(position)
        return positions 



 
# 使用示例
dir_path = './'
data_dict = get_json_data(dir_path)




# 保存data_dict到文件
with open('data_dict.json', 'w', encoding='utf-8') as f:
    json.dump(data_dict, f, ensure_ascii=False, indent=4)
    
    
    
# 遍历并打印合并后的数据
for base_name, positions in data_dict.items():
  #print(f'{base_name}:')
  #print(positions)   
  A,B,C,D=getplane(positions)
  zp=[A,B,C]
  zp=zp/np.linalg.norm(zp)
  #print(np.round(zp,4))
  #print(np.round(np.arccos(zp)/np.pi*180,2))    
  angle3=np.round(np.arccos(zp)/np.pi*180,2)
  print('|',base_name,'|',np.round(zp,4),'|',angle3[0],'|',angle3[1],'|',angle3[2],'|')
  
  
  
  
  
