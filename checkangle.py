import re
import numpy as np

data = """|LPC_CA| [ 0.6297 -0.6935 -0.35 ] | 50.97 | 133.91 | 110.48 |
|LHC_CA| [-0.0217 0.3301 -0.9437] | 91.24 | 70.72 | 160.68 |
|LAC_CA| [-0.7448 -0.5431 -0.3876] | 138.15 | 122.9 | 112.8 |
|LPC_MEM| [ 0.5973 -0.7245 -0.3442] | 53.33 | 136.42 | 110.13 |
|LHC_MEM| [-0.0036 0.3391 -0.9407] | 90.21 | 70.18 | 160.17 |
|LAC_MEM| [-0.7372 -0.5869 -0.3348] | 137.5 | 125.93 | 109.56 |
|LPC_BN| [-0.7469 -0.1077 -0.6562] | 138.32 | 96.18 | 131.01 |
|LHC_BN| [ 0.9723 -0.1052 -0.2087] | 13.52 | 96.04 | 102.05 |
|LAC_BN| [ 0.5364 -0.0841 -0.8397] | 57.56 | 94.82 | 147.11 |"""

pattern = r'\|([\w_]+)\|\s*\[([-\d\s.]+)\]\s*\|\s*(\d+\.\d+)\s*\|\s*(\d+\.\d+)\s*\|\s*(\d+\.\d+)\s*\|'
matches = re.findall(pattern, data)

vectors={}

for match in matches:
    name, vector, x, y, z = match
    vector = [float(num) for num in vector.split()]
    x, y, z = float(x), float(y), float(z)
    print(f"{name}: Vector = {vector}, X = {x}, Y = {y}, Z = {z}")
    vectors[name]=vector


canals=['LHC','LAC','LPC']

for canal in canals:
   bn_name=canal+'_BN'
   bc_name=canal+'_CA'
   mc_name=canal+ '_MEM'
   #print(vectors[bn_name],vectors[bn_name],vectors[mc_name])
   print('|',bn_name+'|',mc_name,'|',np.round(np.arccos(np.dot(vectors[bn_name],vectors[mc_name]))*180/np.pi,2),'|')
   print('|',bn_name+'|',bc_name,'|',np.round(np.arccos(np.dot(vectors[bn_name],vectors[bc_name]))*180/np.pi,2),'|')
   print('|',mc_name+'|',bc_name,'|',np.round(np.arccos(np.dot(vectors[mc_name],vectors[bc_name]))*180/np.pi,2),'|')
   
   
for canal1 in canals:
   for canal2 in canals:
       if canal1 != canal2:
           bn_name1=canal1+'_BN'
           bn_name2=canal2+'_BN'        
           
           print('|',bn_name1+'|',bn_name2,'|',np.round(np.arccos(np.dot(vectors[bn_name1],vectors[bn_name2]))*180/np.pi,2),'|')
        
        
 
for canal in canals:
   bn_name=canal+'_BN'
   bc_name=canal+'_CA'
   mc_name=canal+ '_MEM'
   #print(vectors[bn_name],vectors[bn_name],vectors[mc_name])
   #print('|',bn_name+'|',mc_name,'|',np.round(np.arccos(np.dot(vectors[bn_name],vectors[mc_name]))*180/np.pi,2),'|')
   #print('|',bn_name+'|',bc_name,'|',np.round(np.arccos(np.dot(vectors[bn_name],vectors[bc_name]))*180/np.pi,2),'|')
   #print('|',mc_name+'|',bc_name,'|',np.round(np.arccos(np.dot(vectors[mc_name],vectors[bc_name]))*180/np.pi,2),'|')
   print('|',mc_name+'|',bc_name,'|',vectors[bn_name],'|',vectors[mc_name],'|',np.round(np.arccos(np.dot(vectors[mc_name],vectors[bc_name]))*180/np.pi,2),'|')