from django.shortcuts import render
from django.shortcuts import HttpResponseRedirect,reverse
from django.contrib.auth import authenticate
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from .forms import *
from decimal import Decimal
# Create your views here.
def Login(request):
    message=""
    if request.method=="POST":
        user=authenticate(username=request.POST["username"],password=request.POST["Password"])
        if user!=None:
           login(request,user)
         #  print("DONENENJFDigbdfjgwekq")
           return HttpResponseRedirect(reverse('home'))
        else:
            message="Invalid username or password"
    if  request.user.is_authenticated:
        return HttpResponseRedirect(reverse('home'))
    return render(request,template_name="Login.html" ,context={"msg":message})
def Logout(request):
    logout(request)
    return HttpResponseRedirect(reverse("home"))
def createapharmacy(request):
    form=pharmacyf()
    formi = ""
    if request.user.is_authenticated:
      formi = formimg()
      if request.method=="POST":
        ph=Pharmacy()
        #print(request.POST)
        ph.user=request.user
        ph.Title=request.POST["Title"]
        ph.description=request.POST["description"]
        ph.image=request.FILES["image"]
        #print("ph",ph)
        ph.location=government.objects.get(id=int(request.POST["location"]))
        #print(request.POST["location"],government.objects.get(id=int(request.POST["location"])))
        #print("ph",ph.location)
        ph.save()
        return HttpResponseRedirect(reverse("pharmacy",kwargs={"id":ph.id}))
    else:
        return HttpResponseRedirect(reverse("home"))
    return render(request,template_name="CreateApharmacy.html",context={"form":form,"formi":formi})
def editapharmacy(request,id):
    form=pharmacyf()
    formi = ""
    ph=""
    if request.user.is_authenticated:
      #formi = formimg()
      ph=""
      try:
          ph=Pharmacy.objects.get(id=id,user=request.user)
      except:
          return HttpResponseRedirect(reverse("home"))
      if request.method=="POST":
        #ph=Pharmacy()
        #print(request.POST)
        ph.user=request.user
        ph.Title=request.POST["Title"]
        ph.description=request.POST["description"]
        ph.info_for_accepted_requests=request.POST["info_for_accepted_requests"]
        #print("open",request.POST)
        ph.open=(True if request.POST['open']=="1" else False)
        #ph.image=request.FILES["image"]
        #print("ph",ph)
        ph.location=government.objects.get(id=int(request.POST["location"]))
        #print(request.POST["location"],government.objects.get(id=int(request.POST["location"])))
        #print("ph",ph.location)
        ph.save()
        return HttpResponseRedirect(reverse("pharmacy",kwargs={"id":ph.id}))
    else:
        return HttpResponseRedirect(reverse("home"))
    print("this is ph",ph)
    return render(request,template_name="editpharmacy.html",context={"form":form,"ph":ph,"ph2":ph})
def uploadapharmacy(request,id):
    form=pharmacyf()
    formi = ""
    ph=""
    if request.user.is_authenticated:
      formi = formimg()
      ph=""
      try:
          ph=Pharmacy.objects.get(id=id,user=request.user)
      except:
          return HttpResponseRedirect(reverse("home"))
      if request.method=="POST":
        #ph=Pharmacy()
        #print(request.POST)
        #ph.user=request.user
        #ph.Title=request.POST["Title"]
        #ph.description=request.POST["description"]
        ph.image=request.FILES["image"]
        #print("ph",ph)
        #ph.location=government.objects.get(id=int(request.POST["location"]))
        #print(request.POST["location"],government.objects.get(id=int(request.POST["location"])))
        #print("ph",ph.location)
        ph.save()
        return HttpResponseRedirect(reverse("pharmacy",kwargs={"id":ph.id}))
    else:
        return HttpResponseRedirect(reverse("home"))
    return render(request,template_name="editpharmacy.html",context={"form":formi,"ph":"","ph2":ph})

def homepage(request):
    gv="all"
    phs=list(Pharmacy.objects.all().order_by('-feed'))
    gev=list(government.objects.all())
    return render(request,template_name="home.html",context={"phs":phs,"gev":gev,"gv":gv})
def homepage2(request,l):
    gv=government.objects.get(id=l)
    phs=list(Pharmacy.objects.filter(location=gv).order_by('-feed'))
    gev = list(government.objects.all())
    return render(request,template_name="home.html",context={"phs":phs,"gev":gev,"gv":gv})

def pharmacyshow(request,id):
    ph=Pharmacy.objects.get(id=id)
    feed=""
    feeds=""
    ee=False
    g=True
    try:
        feeds = list(feedback.objects.filter(phid=ph))
    except:
        []
    try:

        feed = feedback.objects.get(phid=ph, user=request.user)
        fd=feed

        #print(feeds)
    except:
        fd=feedback()
        g=False
    #print(request.POST)
    e=False
    if request.user.is_authenticated:
        try:
            rr=workrequest.objects.get(phid=id,user=request.user)
            if rr.accepted==True:
                ee=True
        except:
            ee=False
        try:
            if ph == Pharmacy.objects.get(id=id, user=request.user):
                e=True
                ee=True
        except:
            e=False
        if request.method=="POST":
                fd.phid=ph
                oldv=fd.value
                fd.value = Decimal(request.POST["feed"])
                fd.Comment=request.POST["comment"]
                fd.user=request.user
                #print(fd.Comment)
                #print(fd,fd.phid,fd.comment,fd.value,fd.user)
                fd.save()
                #if g:
                phfeed=0.
                n=0
                y=list(feedback.objects.filter(phid=ph))
                for t in y:
                    phfeed+=float(t.value)
                    n+=1
                ph.feed=Decimal(phfeed)/n
                ph.numoffeeds=n
                ph.save()
                #else:
                 #   ph.feed = (ph.feed * ph.numoffeeds + fd.value) / (ph.numoffeeds + 1)
                #ph.numoffeeds += 1
                #ph.save()
                feed=fd
                feeds = ph.feedback_set.all()
    return render(request,template_name="pharmacy.html",context={"ph":ph,'feed':feed,"feeds":feeds,"usr":User,"e":e,"ee":ee,"f":int(ph.numoffeeds)})
def register(request):
    msg=""
    formg=selectgender()
    if not request.user.is_authenticated:
        #print('create1')
        if request.method=='POST':
         #   print('create2')
            if request.POST['password']==request.POST['confirm']:
               user=User.objects.create_user(request.POST['yourname'], request.POST['email'], request.POST['password'])
               pr=profileinfo()
               pr.user=user
               pr.location=government.objects.get(id=1)
               pr.First_name=request.POST['firstn']
               pr.Last_name=request.POST['lastn']
               pr.gender=genders.objects.get(id=int(request.POST['gender']))
               pr.save()
               return HttpResponseRedirect(reverse("login"))
            else:
                msg="password didn't match"

                return render(request, template_name='register.html', context={"msg": msg})
            return HttpResponseRedirect(reverse('login'))
        else:
             return render(request,template_name='register.html',context={"msg":msg,"formg":formg})
    return HttpResponseRedirect(reverse("home"))
def requestwork(request,phid):
    form=""
    msg="You need an account to use this feature"
    w=""
    ph = ""
    vv=""
    if request.user.is_authenticated:
        try:
            ph=Pharmacy.objects.get(id=phid)
            r=workrequest.objects.get(phid=phid,user=request.user)
        except:
            r=""
        #print("this is r ",r)
        form = requestform()
        msg = ""
        vv = "submit"
        if request.method=="POST" and r=="" and ph!="" and ph.open==True:

            w=workrequest()
            w.phid=Pharmacy.objects.get(id=phid)
            w.user=request.user
            w.workertype=worker.objects.get(id=request.POST["workertype"])
            w.shifttype=shift.objects.get(id=request.POST["shifttype"])
            w.requesttext=request.POST["requesttext"]
            w.accepted=False
            w.save()
            form=""
            vv="delete"
        elif r!="":
            form=""
            vv = "delete"
            w = r
            if request.method == "POST":
                r.delete()
                form=requestform()
                w=""
                vv="submit"
        else:
            []#return HttpResponseRedirect(reverse("home"))
    return render(request,template_name="request.html",context={"form":form,"w":w,"msg":msg,"ph":ph,"vv":vv})
def requestview(request,id):
    form=""
    msg="You need an account to use this feature"
    w=""
    ph = ""
    vv=""
    if request.user.is_authenticated:
        try:
            r=workrequest.objects.get(id=id)
            ph=r.phid
            if ph.user!=request.user:
                r=""
        except:
            r=""
        if r!="":
            vv = ""
            w = r
        else:
            return HttpResponseRedirect(reverse("home"))
    else:
            return HttpResponseRedirect(reverse("home"))
    return render(request,template_name="request.html",context={"form":form,"w":w,"msg":msg,"ph":ph,"vv":vv})
def viewrequests(request,tr):
    lista = []
    if request.user.is_authenticated:
        try:
            ph=Pharmacy.objects.filter(user=request.user)
            for p in ph :
                lista.append(list(workrequest.objects.filter(phid=p)))
        except:
            []#print("errrrrrrrrrrrrrrrrrrrrrrrrrr\n\n\n\n")
    return render(request,template_name="viewrequests.html",context={"lis":lista,"tr":tr})
def refuserequest(request,rid):
    if request.user.is_authenticated:
        r=workrequest.objects.get(id=rid)
        ph=r.phid
        if ph.user==request.user:
            r.refused=True
            r.accepted=False
            r.save()
        return HttpResponseRedirect(reverse("viewrequests",kwargs={"tr":"pending"}))
    return HttpResponseRedirect(reverse("home"))
def acceptrequest(request,rid):
    if request.user.is_authenticated:
        r=workrequest.objects.get(id=rid)
        ph=r.phid
        if ph.user==request.user:
            r.accepted=True
            r.refused=False
            r.save()
        return HttpResponseRedirect(reverse("viewrequests",kwargs={"tr":"pending"}))
    return HttpResponseRedirect(reverse("home"))
def editprofile(request):
    msg=""
    info=""
    form=""
    if request.user.is_authenticated:
        pr = profileinfo.objects.get(user=request.user)
        info=pr
        form=formimg()
        form2=profileinfof()
        if request.method=="POST":
            pr.First_name=request.POST['First_name']
            pr.Last_name=request.POST['Last_name']
            pr.About=str(request.POST['About'])
            pr.Age=int(request.POST['Age'])
            #pr.image=request.FILES['image']
            pr.location = government.objects.get(id=int(request.POST["location"]))
            pr.save()
            request.user.email=request.POST['email']
            request.user.save()
            msg="informations updated"
    return render(request,template_name="editprofile.html",context={"msg":msg,"info":info,"form":form,"form2":form2})
def uploadprofile(request):
    msg=""
    info=""
    form=""
    if request.user.is_authenticated:
        pr = profileinfo.objects.get(user=request.user)
        #info=pr
        form=formimg()
        #form2=profileinfof()
        if request.method=="POST":
            #pr.First_name=request.POST['firstn']
            #pr.Last_name=request.POST['lastn']
            #pr.About=str(request.POST['about'])
            pr.image=request.FILES['image']
            #pr.location = government.objects.get(id=int(request.POST["location"]))
            pr.save()
            #request.user.email=request.POST['email']
            #request.user.save()
            msg="informations updated"
            return  HttpResponseRedirect( reverse("profile",kwargs={"id":request.user.id}) )
    return render(request,template_name="uploadprofile.html",context={"msg":msg,"info":info,"form":form})

def profile(request,id):
    info=""
    e=False
    myuser=""
    #if request.user.is_authenticated:
    try:
        myuser=User.objects.get(id=id)
        pr = profileinfo.objects.get(user=myuser)
        info=pr
        if request.user.is_authenticated:
            if request.user.id==id:
                e=True
    except:
        []
    return render(request, template_name="profile.html", context={"info": info,"e":e,"myuser":myuser})