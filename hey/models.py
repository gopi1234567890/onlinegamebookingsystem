from django.db import models

# Create your models here.
class game:
    def __init__(self,name,photo,side,dis):
        self.photo=photo
        self.name=name
        self.side=side
        self.dis=dis

l=[]
g=[game('valo','','',''),game('apex','','',''),game('minecraft','','',''),game('overwatch','','',''),game('gta5','','','')]
users=[]
class branch:
    def __init__(self,name,n,g,s):
        self.name=name
        self.n=n
        self.g=g
        self.d={}
        for i in s:
            self.d[i]=[]
            
day=list('monday tuesday wednesday tuesday friday satureday'.split())
b=[branch('hyderabad',3,[g[0].name,g[3].name],day),branch('kukatpally',2,[g[0].name,g[1].name,g[2].name],day)]
duration=list(map(int,'1 2 3 4'.split()))


re={'email':['username','first_name','last_name','password']}
