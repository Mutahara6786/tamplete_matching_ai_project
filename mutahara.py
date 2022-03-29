import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import matplotlib.patches as patches
from PIL import Image,ImageFilter
from numpy.lib.function_base import average
import numpy as np
import scipy.stats
import random

img = Image.open('group.jpg')
img1 = Image.open('boothi.jpg')
img1_array=np.array(img)
img2_array=np.array(img1)
avg1=[]
SUM=0
pop=[]
fit=[]
m=[]
n=[]
GeneratoionNo=0
width, height = img.size
width1, height1 = img1.size


def population(x):
    size=x
    for i in range(size):
        m=random.randint(0,width-width1)
        n=random.randint(0,height-height1)
        pop.append([m,n])
    print("number of generation is..............." ,GeneratoionNo )
    return pop


def fittness():
    for i in pop:
        slice=img1_array[i[1]:i[1]+height1,i[0]:i[0]+width1]
        fit.append([scipy.stats.kendalltau(img2_array, slice).correlation,i[0],i[1]])
    fit.sort(key = lambda x: x[0], reverse=True)



def fittness1(x,y):
    slice=img1_array[y:y+height1,x:x+width1]
    return scipy.stats.kendalltau(img2_array, slice).correlation


def display(x,y):
   
    fig,ax = plt.subplots(1)
    rect = patches.Rectangle((x,y),width1,height1, edgecolor='b', facecolor="none")

    ax.imshow(img1_array,cmap="gray")
    ax.add_patch(rect)
    plt.show()


def bits(x):
    if(10-len(x)>0):
        z=10-len(x)
        x=('0'*z)+x
    return x

def cross_bits(x1,y1,x2,y2):
    if(10-len(x1)>0):
        z=10-len(x1)
        x1=('0'*z)+x1

    if(10-len(y1)>0):
        z=10-len(y1)
        y1=('0'*z)+y1

    if(10-len(x2)>0):
        z=10-len(x2)
        x2=('0'*z)+x2

    if(10-len(y2)>0):
        z=10-len(y2)
        y2=('0'*z)+y2
    return x1,y1,x2,y2

size=150
correlation=0.55
pop=population(size)
fittness()
while(fit[0][0]<correlation):

    fittness()
    GeneratoionNo+=1
    print("..............................................")
    print("Number of generation is. ",GeneratoionNo)
    m.append(GeneratoionNo)
    n.append(fit[0][0])
    for l in range(len(fit)):
        SUM=SUM+fit[l][0]
    average=SUM/len(fit)
    avg1.append(average)
    SUM=0
    print("the average of corelation is................... ",average)
    print("-----------------")
plt.plot(m, n)
plt.plot(avg1)
display(fit[0][1],fit[0][2])
