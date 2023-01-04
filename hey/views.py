
from django.shortcuts import render,redirect
from .models import l,re,users,day,duration,g,b
import smtplib
import ssl
from email.message import EmailMessage
sender='  gz7755831@gmail.com    '
password='cuecymeefdloncjg'
time={}

for i in range(1,24):
    if(i>12):
        time[i]=i -12
    else:
        time[i]=i

def gl(request):
    return render(request,'gl.html')
# Create your views here.
def login(request):
    da=request.POST
    # chech with the details  in teh data base 

    if(da):
        users.append(da['email'])
       
        return render(request,'index.html',{'t':users[-1],'b':b,'g':g,'day':day,'duration':duration,'time':time})
    
    return render(request,'login.html')



def regis(request):
    if(request.POST):
        da=request.POST
        if(request.POST['email'] not  in re):
            if(da['password']==da['confirm_password']):
                re[request.POST['email']]=[]
                for i in da:
                    if(i in re['email']):
                        re[request.POST['email']].append(da[i])
                print(da['email'],'///////')
                em=EmailMessage()
                em['From']=sender
                em['To']=da['email']
                em['Subject']='u got registered '
                b=""" hey dude u got registered in the website called as gamezone 
                thanks for the  registering """
                em.set_content(b)
                co=ssl.create_default_context()
                with smtplib.SMTP_SSL('smtp.gmail.com',465,context=co) as smtp:
                    smtp.login(sender,password)
                    smtp.sendmail(sender,da['email'],em.as_string())

                return redirect('login')

            else:
                #password does not match
                return render(request,'acr.html',{'t':['dude passwor does not match ']})
        else:
            # email is present
            return render(request,'acr.html',{'t':['u there bro']})
    else:
        return render(request,'regis.html')




def search(request):
    # searching the game  
    # found 
    #return render(request,'no.html')
    da=request.POST
    
    if(len(da)==1):

        return redirect('index')
    for i in b:
        print('////@@@/',i.name)
        if(i.name==da['branch'] and da['game'] in i.g):
            st=int(da['time'])
            en=st+int(da['duration'])
            if(len(i.d[da['day']])==0):
                i.d[da['day']].append([[st,en]])
                s=[da['branch'],da['game'],da['time'],da['duration']]
                return render(request,'yes.html',{'t':users[-1],'b':b,'g':g,'day':day,'duration':duration,'time':time})
            else:
                
              
                for p in  range(len(i.d[da['day']])):
                    g1=[]
                    for j in range(25):
                        g1.append(0)
                    y=1
                    for  j in i.d[da['day']][p]:
                        if((st>=j[0] and st<j[1]) or ( en>j[0] and en<=j[1])):
                            ## change tjhe slot becaise u dont ahvce 
                            y=0
                            break

                        else:    
                            for j1 in range(j[0],j[1]):
                                g1[j1]=-1
                            
                    if(y!=0):
                        
                        for j in range(st,en+1):
                            if(g1[j]==-1):
                                y=0
                                break
                        

                     # u r good to go  
                    if(y==1): 
                        i.d[da['day']][p].append([st,en])
                        s=[da['branch'],da['game'],da['time'],da['duration']]
                        print(i.d[da['day']])
                        return render(request,'yes.html',{'t':users[-1],'b':b,'g':g,'day':day,'duration':duration,'time':time})
                if(len( i.d[da['day']])<i.n):
                    i.d[da['day']].append([[st,en]])
                    s=[da['branch'],da['game'],da['time'],da['duration']]
                    print(i.d[da['day']])
                    return render(request,'yes.html',{'t':users[-1],'b':b,'g':g,'day':day,'duration':duration,'time':time})
                return render(request,'no.html',{'t':users[-1]})
        
            # nogame 
    return render(request,'no.html',{'t':users[-1]})

    
def index(request):
    
    return render(request,'index.html',{'t':users[-1],'b':b,'g':g,'day':day,'duration':duration,'time':time})
def check(request):
    da=request.POST
    for i in da:
        print(i )
    return redirect('login')
def profile(request):
    return render(request,'profile.html',{'t':users[-1]})
def contact(request):
    return render(request,'contact.html',{'t':users[-1]})
def games(request):
    return render(request,'games.html',{'t':users[-1]})