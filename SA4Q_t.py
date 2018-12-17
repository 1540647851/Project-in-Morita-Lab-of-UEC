import AD
import random as rnd
import time
import numpy as np

def sfxbox(T):
    dic=AD.strsort(list(set(T)))
    ld=len(dic)
    dicc=[0]*ld
    for i in range(len(T)):
        for j in range(ld):
            if T[i]==dic[j]:
                dicc[j]+=1
    mk=0
    box=[]
    boxes=[]
    for i in range(ld):
       box.append(mk)
       mk=mk+dicc[i]
       box.append(mk-1)
       boxes.append(box)
       box=[]
    return boxes
    
def DamnedPairs(T,newsymbol,sa,l):
    #ns=new symbol
    while 1:
        t=0
        #la=AD.lcpary(T,sa) #Costs too much time (99.9%)
        for i in range(l-1):
            lt=l-sa[i]
            p=sa[i+1]+lt
            if p>=l:
                sb=""
            else:
                sb=T[p]
            if (newsymbol>sb) and (T[sa[i]:]==T[sa[i+1]:sa[i+1]+lt]):
                sa[i],sa[i+1]=sa[i+1],sa[i]
                t=t+1
        if t==0:
            break
        
def Insertnsfx(T,ns,sa,l):
    n=0
    for i in range(l):
        if T[l-1-i]==ns:
            n=n+1
        else: break
    if n==0:
        mk=0
        for i in range(l):
            if ns<T[sa[i]:]:
                break
            mk+=1
        if i+1==l and mk==l:
            i+=1
        sa.insert(i,l)
    else:
        for i in range(l):
            if T[sa[i]]==ns:
                sa.insert(i,l)
                break

def sfxary4n(T,ns,sa):
    #suffix array for new string
    l=len(T)
    DamnedPairs(T,ns,sa,l)
    Insertnsfx(T+ns,ns,sa,l,)
    sa.remove(0)
    for i in range(len(sa)):
        sa[i]-=1
    return sa

def slidingsfxary(T,w,l):
    sa=AD.sfxary(T[:w])
    for i in range(l-w):
#        print(T[i:i+w],end=" ");print(T[i+w])
        sfxary4n(T[i:i+w],T[i+w],sa)
        sa=sa
    

#Test---------------------------------------------------------------------------
#def tst(dic,n):#generate random text from "dic" to test
#    rdmstr=""
#    for i in range(n):
#        rdmstr=rdmstr+dic[rnd.randint(0,len(dic)-1)]
#    new="".join(dic[rnd.randint(0,len(dic)-1)])
#    sa=AD.sfxary(rdmstr)
#    t0=time.time()
#    sa0=AD.sfxary((rdmstr+new)[1:])
#    t1=time.time()
#    sa1=sfxary4n(rdmstr,new,sa)
#    t2=time.time()
#    return sa0==sa1,rdmstr,t1-t0,t2-t1
#
#def Test(length,times=1):
#    #length is the length of testing text, times is testing times
#    failure=[];timeold=[];timenew=[];
#    for i in range(times):
#        [a,b,t0,t1]=tst("0123456789",length)
#        timeold.append(t0)
#        timenew.append(t1)
#        if a==False:
#           failure.append(b)
#    a0=np.mean(timeold)
#    a1=np.mean(timenew)
#    return failure,a0,a1,str(round(a1*100/a0,2))[:]+"%"

#Test---------------------------------------------------------------------------
def slidingsfxary_old(T,w,l):
    for i in range(l-w):
#        print(T[i:i+w],end=" ");print(T[i+w])
        sa=AD.sfxary(T[i+1:i+w+1])
        sa=sa

def test(n,ws):
#windowsize_array, for eg: [100,1000,2000,5000,10000]
    dic="0123456789"
    rdmstr=""
    for i in range(n):
        rdmstr=rdmstr+dic[rnd.randint(0,len(dic)-1)]
    l=len(ws)
    for i in range(l):
        w=ws[i]
        t0=time.time()
        slidingsfxary(rdmstr,w,n)
        t1=time.time()
        slidingsfxary_old(rdmstr,w,n)
        t2=time.time()
        ws[i]=[ws[i],(t1-t0)/(t2-t1)]
    return np.array(ws)
#[failure,timeold,timenew,η]=Test(10,100)
##failure:the failure position array
##timeold:Redo algorithm time costs(average among all the testing string)
##timenew:Sliding method time costs(average among all the testing string)
##η:timenew/timeold*100%
#print()
#if len(failure)==0:
#    #If failure array is void, means success
#    print("!!SUCCEED!!")
#print("With the time costs {pct} of Redo algorithm".format(pct=η))

#T="12312323342123123"
#sfx=AD.strsort(AD.sfx(T))
#sa=AD.sfxary(T)
#sa=np.array(sa).tolist()
#s1=sfxary4n(T,"2",sa)
#s2=AD.sfxary(T+"2")
#newsymbol="3"
#for i in range(len(T)-1):
#    lt=len(T[sa[i]:])
#    p=sa[i+1]+lt
#    if p>=len(T):
#        sb=""
#    else:
#        sb=T[p]
#    print(i,end=".")
#    print(newsymbol>sb and T[sa[i]:]==T[sa[i+1]:sa[i+1]+lt])
ws=[2**x*100 for x in range(0,5)]
a=test(10000,ws)