# -*- coding: utf-8 -*-
import AD
import random as rnd
from time import time
import numpy as np

def rnkary(sa,l=0):
    if l==0:
        l=len(sa)
    rank=[0]*l
    j=0
    for i in sa:
        rank[i]=j
        j+=1
    return rank

def lcp(T,a,b,s=0,l=0):
    if l==0:
        l=len(T)
    if s<0:
        s=0
    t1,t2=T[a:],T[b:]
    ml=s
    for i in range(s,l-max(a,b)):
        if t1[i]==t2[i]:
            ml+=1
        else:
            break
    return ml
    


def lcpary(T,sa,l=0):
    
    if l==0:
        l=len(T)
    la=[0]*(l-1)
    t0=time()
    ra=rnkary(sa,l) #——————————consume most time
    t1=time()
    ra.remove(l-1)

    i=0
    idx=ra[i]
    la[idx]=lcp(T,sa[idx],sa[idx+1])
    oidx=idx
    
    for i in range(1,l-1):
        idx=ra[i]
        la[idx]=lcp(T,sa[idx],sa[idx+1],la[oidx]-1)
        oidx=idx
    
    return la,(t1-t0)

#T="1212341342441513142544312"
##T="01011"
#sa=AD.sfxary(T)
#n=lcpary(T,sa)
#o=AD.lcpary(T)
#srt=AD.strsort(AD.sfx(T))
#print(rnkary(sa))
def tst(dic,n):
    rdmstr=""
    for i in range(n):
        rdmstr=rdmstr+dic[rnd.randint(0,len(dic)-1)]
    sa=AD.sfxary(rdmstr)
#    t0=time()
    olcpa=AD.lcpary(rdmstr,sa)
#    t1=time()
    [nlcpa,t]=lcpary(rdmstr,sa,n)
#    t2=time()
    return [olcpa==nlcpa,t]

def test(l):
    failure=[]
    time=[]
    for i in range(len(l)):
        [c,t]=tst("0123456789",l[i])
        time.append([l[i],t])
    time=np.array(time)
    return failure,time

l=[200,400,800,1600,3200,6400]
[failure,t]=test(l)

        
