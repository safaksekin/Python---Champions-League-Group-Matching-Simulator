import random
def set_pot(pot_list,len,len_group):
    pass

def line1(group,len):
    value=random.randint(0,len-1)
    group.append(pot1[value])
    pot1.pop(value)

def line2(group,len):
    value=random.randint(0,len-1)
    if group[0].nation != pot2[value].nation:
        group.append(pot2[value])
        pot2.pop(value)
    else:
        line2(group,len)

def line3(group,len):
    value=random.randint(0,len-1)
    if group[0].nation == pot3[value].nation:
        line3(group,len)
    elif group[1].nation == pot3[value].nation:
        line3(group,len)
    else:
        group.append(pot3[value])
        pot3.pop(value)

def line4(group,len):
    value=random.randint(0,len-1)
    if group[0].nation == pot4[value].nation:
        line4(group,len)
    elif group[1].nation == pot4[value].nation:
        line4(group,len)
    elif group[2].nation == pot4[value].nation:
        line4(group,len)
    else:
        group.append(pot4[value])
        pot4.pop(value)






class team():
    def __init__(self,name,nation):
        self.name=name
        self.nation=nation

che=team("che","england")
vil=team("vil","spain")
bay=team("bay","germany")
mnc=team("mnc","england")
atm=team("atm","spain")
int=team("int","italy")
liz=team("liz","portugal")
lil=team("lil","france")

rma=team("rma","spain")
bar=team("bar","spain")
juv=team("juv","italy")
mnu=team("mnu","england")
psg=team("psg","france")
liv=team("liv","england")
sev=team("sev","spain")
bvb=team("bvb","germany")

por=team("por","portugal")
ajx=team("ajx","netherlands")
shk=team("shk","ukrain")
lei=team("lei","germany")
slz=team("slz","austria")
ben=team("ben","portugal")
ata=team("ata","italy")
zen=team("zen","russia")

bjk=team("bjk","turkey")
dkv=team("dkv","ukrain")
cbg=team("cbg","belgium")
yng=team("yng","sweden")
acm=team("acm","italy")
mal=team("mal","sweden")
wol=team("wol","germany")
she=team("she","moldovia")





pot1=[che,vil,bay,mnc,atm,int,liz,lil]
pot2=[rma,bar,juv,mnu,psg,liv,sev,bvb]
pot3=[por,ajx,shk,lei,slz,ben,ata,zen]
pot4=[bjk,dkv,cbg,yng,acm,mal,wol,she]

A=[]
B=[]
C=[]
D=[]
E=[]
F=[]
G=[]
H=[]

len_1=8
len_2=8
len_3=8
len_4=8


group_list=[A,B,C,D,E,F,G,H]

#GROUP A
line1(A,8)
line2(A,8)
line3(A,8)
line4(A,8)
#GROUP B
line1(B,7)
line2(B,7)
line3(B,7)
line4(B,7)
#GROUP C
line1(C,6)
line2(C,6)
line3(C,6)
line4(C,6)
#GROUP D
line1(D,5)
line2(D,5)
line3(D,5)
line4(D,5)
#GROUP E
line1(E,4)
line2(E,4)
line3(E,4)
line4(E,4)
#GROUP F
line1(F,3)
line2(F,3)
line3(F,3)
line4(F,3)
#GROUP G
line1(G,2)
line2(G,2)
line3(G,2)
line4(G,2)
#GROUP H
H.append(pot1[0])
H.append(pot2[0])
H.append(pot3[0])
H.append(pot4[0])







print("---GROUP A---")
print(str(A[0].name)+"\n"+str(A[1].name)+"\n"+str(A[2].name)+"\n"+str(A[3].name))
print("-------------")
print("---GROUP B---")
print(str(B[0].name)+"\n"+str(B[1].name)+"\n"+str(B[2].name)+"\n"+str(B[3].name))
print("-------------")
print("---GROUP C---")
print(str(C[0].name)+"\n"+str(C[1].name)+"\n"+str(C[2].name)+"\n"+str(C[3].name))
print("-------------")
print("---GROUP D---")
print(str(D[0].name)+"\n"+str(D[1].name)+"\n"+str(D[2].name)+"\n"+str(D[3].name))
print("-------------")
print("---GROUP E---")
print(str(E[0].name)+"\n"+str(E[1].name)+"\n"+str(E[2].name)+"\n"+str(E[3].name))
print("-------------")
print("---GROUP F---")
print(str(F[0].name)+"\n"+str(F[1].name)+"\n"+str(F[2].name)+"\n"+str(F[3].name))
print("-------------")
print("---GROUP G---")
print(str(G[0].name)+"\n"+str(G[1].name)+"\n"+str(G[2].name)+"\n"+str(G[3].name))
print("-------------")
print("---GROUP H---")
print(str(H[0].name)+"\n"+str(H[1].name)+"\n"+str(H[2].name)+"\n"+str(H[3].name))
