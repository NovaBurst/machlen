import numpy as np
class person:
    def __init__(self,height=0.0,weight=0.0,sex='u'):
        self.height=height
        self.weight=weight
        self.sex=sex
    def outputperson(self):
        print(self.height)
        print(self.weight)
        print(self.sex)

def read_person(line,sample=False):
    t=line.split()
    height=t[0]
    weight=t[1]
    sex=t[2].upper()
    if (sample==False):#sex included
        return person(height,weight,sex)
    else:
        return person(height,weight)

def makearray(ps,b=1):
    h,w=ps.height,ps.weight
    if (ps.sex=='F'):
        s=1
    else:
        s=-1
    rst=list()
    rst.append((float)(b))
    rst.append((float)(h))
    rst.append((float)(w))
    #print(rst)
    return rst

def readsex(line):
    t=line.split()
    sex=t[2].upper()
    if (sex=='M'):
        return -1
    else:
        return 1
    

def openfile(filename='/Users/apple/Documents/ml/dataset1.txt'):
    rst=open(filename,mode='r')
    return rst
    
           
def makex(filein):
        x=list()
        for line in filein:
            x.append(makearray(read_person(line)))
        return x

def maked(filein):
    d=list()
    for line in filein:
        d.append(readsex(line))
    return d


b=0
a=0.3
xx=makex(openfile())
dd=maked(openfile())
x=np.array(xx)
d=np.array(dd)
#x=np.array([[b,167,52],[b,170,50],[b,160,45],[b,172,67],[b,158,45],[b,170,60]])
#d=np.array([1,1,-1,-1,1,-1])
w=np.array([1,0,0])
def sgn(v):
    if (v>=0):
        return 1
    else:
        return -1

def comy(myw,myx):
    return sgn(np.dot(myw.T,myx))

def neww(oldw,myd,myx,a):
    #print (comy(oldw,myx))
    return oldw+a*(myd-comy(oldw,myx))*myx

i=0
for xn in x:
    #print (xn)
    w=neww(w,d[i],xn,a)
    i+=1
    #print (w)
for xn in x:
    pass
    #print ("%d %d => %d"%(xn[1],xn[2],comy(w,xn)))
test=np.array([1,167,52])
print("%f %f => %f"%(test[1],test[2],comy(w,test)))
           



              
