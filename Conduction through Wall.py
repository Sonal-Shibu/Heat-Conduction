"""
Conduction Through Walls
"""
import numpy as np
#%%
TA=input("Enter the temperature of the hot side of the system ") #oC
TB=input("Enter the temperature pf the cold side of the system ") #oC

NumWalls=input("Enter the number of wall for this system " )
#Area= #m^2

hA=input("Enter the convective heat transfer coefficient of the hot side ")
hB=input("Enter the convective heat transfer coefficient of the Cold side ")

A=input("Enter the Area of the system, NOT THE THICKNESS! ")

TA=float(TA)
TB=float(TB)
NumWalls=int(NumWalls)
hA=float(hA)
hB=float(hB)
A=float(A)
#%%
Wall_Thickness=np.zeros(NumWalls)
Wall_ThermCond=np.zeros(NumWalls)

R_Walls=np.zeros(NumWalls)

for i in range(0,(NumWalls)):
    print("Enter the wall thickness for wall ",i+1," ")
    Wall_Thickness[i]=input()
    
for i in range(0,(NumWalls)):
    print("Enter the wall Thermal Conductivity for wall ",i+1," ")
    Wall_ThermCond[i]=input()


for i in range(0,NumWalls):
    R_Walls[i]=Wall_Thickness[i]/(A*Wall_ThermCond[i])

R_total=(np.sum(R_Walls))+(1/hA*A)+(1/hB*A)

Q=((TA-TB)/R_total)

print("The heat transfer through the wall is ",Q," Watts")
#%%
Temp_Surf=np.zeros(NumWalls-1)
T1= ((Q-A*hA*TA)/(A*hA))*-1
TEND= (Q/(A*hB))+TB

Temp_Surf[0]=( ( ( Q*Wall_Thickness[0] ) - ( A*Wall_ThermCond[0]*T1 ) )/( A*Wall_ThermCond[0] ) ) *-1

for i in range(1,NumWalls-1):
    #print(i)
    Temp_Surf[i]=( ( ( Q*Wall_Thickness[i] ) - ( A*Wall_ThermCond[i]*Temp_Surf[i-1] ) )/( A*Wall_ThermCond[i] ) )*-1
    
Temp_Surf=np.insert(Temp_Surf,0 , T1)
Temp_Surf=np.append(Temp_Surf, TEND)

Temp_Dist=np.array([TA])     
Temp_Dist=np.append(Temp_Dist, Temp_Surf)
Temp_Dist=np.append(Temp_Dist, TB)

print("This is the Temperature Distribution through: ",np.round(Temp_Dist,2))