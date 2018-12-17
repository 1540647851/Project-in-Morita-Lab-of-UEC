#suffix array generate---------------------------------------------------------
def sfx(s):
    return [s[i:] for i in range(0,len(s))]

def strsort(str):  
    tmp = [(x,x) for x in str]
    tmp.sort()
    return [x[1] for x in tmp]

def sfxary(bstr):
    sfxd=sfx(bstr)
    l=len(sfxd)
    stsfxd=strsort(sfxd)
    s=[0]*l
    for i in range(l):
        s[i]=sfxd.index(stsfxd[i])
    return s


#LCP array generate------------------------------------------------------------
def lcp(i, j, T, SA):
	imin=len(T)-max(SA[i],SA[j])
	a=T[SA[i]:]
	b=T[SA[j]:]
	k=0
	while a[k]==b[k]:
		k+=1
		if (k>=imin):
			break
	return k

def lcpary(T,SA=1):
    if SA==1:
        SA=sfxary(T)
    LCP=[]
    for i in range(len(T)-1):
        LCP.append(lcp(i,i+1,T,SA))
    return LCP



#Generate MFWs-------------------------------------------------------
def possiblesub(T):
    #Possible substrings that may be MFWs (Theorem 3)
    l=len(T)
    uj=[0]*2*l
    sa=sfxary(T)
    la=lcpary(T)
    la.append(0)
    la.insert(0,0)
    for i in range(l):
        uj[2*i]=[sa[i],sa[i]+la[i]]
        uj[2*i+1]=[sa[i],sa[i]+la[i+1]]
        #Two possible length of prefix
    uj=uj[:2*l-1]
    return uj 
    #return the begin and end index of possible substrings.
    
def headset(begin,end,T):
    #Calculate the headset of a substring T[begin:end+1],(T is the original string)
    alphabet=set()
    for i in range(len(T)):
        alphabet.add(T[i])
    alphabet=list(alphabet)
    #each element in a set is unique, use this feature to build alphabet{}
    l=len(alphabet)
    hds=[]
    t=T[begin:end+1]
    for i in range(l):
        tt=alphabet[i]+t
        if tt in T:#if  "alphabet[i]t" appears 
            hds.append(alphabet[i])
    return hds

def mfw(index,T):
    #use Theorem 1 to generate MFW
    H=list(set(headset(index[0],index[1]-1,T))-set(headset(index[0],index[1],T)))
    #Do the minus calculation between two sets
    l=len(H)
    w=[0]*l
    for i in range(l):
        w[i]=H[i]+T[index[0]:index[1]+1]
    return w

from itertools import chain#Flatten, from Morita sense's lecture
def flatten(listOfLists):
    "Flatten one level of nesting"
    return list(chain.from_iterable(listOfLists))

def ad(T):
    u=possiblesub(T)#calculate all the possible substrings that could be MFWs
    ad=[]
    for i in range(len(u)):
        ad.append(mfw(u[i],T))
        #generate MFW for each possible substring
    return list(set(flatten(ad)))
            #To remove redundant MFWs

#Test++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
"""
T="abcdefghijklmnopqrstuvwxyz0123456789"
alphabet=set()
for i in range(len(T)):
    alphabet.add(T[i])
alphabet=list(alphabet)

alphabet=['0','1']
def txtgen(n):
    global alphabet
    txt=""
    for i in range(n):
        txt=txt+alphabet[random.randint(0,1)]
    return txt

def tst():
    n=[2**n for n in range(3,15)]
    t=[]
    for i in range(12):
        txt=txtgen(n[i])
        t1=time.time()
        possiblesub(txt)
        t2=time.time()
        t.append(t2-t1)
    return n,t
[n,t]=tst()
"""