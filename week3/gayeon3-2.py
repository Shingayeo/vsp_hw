import matplotlib.pyplot as plt 
import matplotlib.patches as patches

pnt_x = 5
pnt_y = 3

fig, axes = plt.subplots(1,1,figsize=(5,5)) #figsize는 보통 가로세로 비율을 맞출 때 씀

plt.plot(pnt_x, 
         pnt_y,
         marker = 'o' ) #점 찍기

plt.show()

r=2

cir = patches.Circle( (pnt_x, pnt_y), r)
axes.add_patch(cir)

plt.show()