from django.shortcuts import render
from django.http import HttpResponse
from . models import *
from django.db.models import Q
from datetime import datetime
# Create your views here.
def index(request):
    data=category.objects.all().order_by('-id')[0:6]
    sliderdata=slider.objects.all().order_by('-id')[0:3]
    carddata=card.objects.all().order_by('-id')[0:3]
    mdata=events.objects.all().order_by('-id')[0:8]
    edata=evnames.objects.all().order_by('-id')[0:8]
    md={"cdata":data,"sldata":sliderdata,"cadata":carddata,"edata":edata,"mdata":mdata}
    return render(request,'user/index.html',md,)
def login(request):
    if request.method=="POST":
        email=request.POST.get('email')
        passwd=request.POST.get('passwd')
        x=register.objects.filter(email=email,passwd=passwd).count()
        if x==1:
            a=register.objects.filter(email=email,passwd=passwd)
            request.session['username']=str(a[0].name)
            # request.session['userpic']=str(a[0].upic)
            request.session['user']=email
            return HttpResponse("<script>alert('You are signed In');location.href='/user/index/'</script>")
        else:
            return  HttpResponse("<script>alert('Your userid or password is incorrect');location.href='/user/signin/'</script>")
    return render(request,'user/login.html')

def logout(request):
    user=request.session.get('user')
    if user:
        del request.session['user']
        del request.session['username']
        return HttpResponse("<script>alert('You are logout successfully');location.href='/user/index/'</script>")
    return render(request,"user/logout.html")

def feedback(request):
    if request.method =="POST":
        name=request.POST.get('name')
        email= request.POST.get('email')
        msg= request.POST.get('msg')
        #print(a1,a2,a3,a4)
        feedbacks(name=name,email=email,msg=msg,).save()
        return HttpResponse("<script> alert('Thank You for your feedback ');location.href='/user/feedback/'</script>")
    return render(request,'user/feedback.html')

def home(request):
    return render(request,'user/home.html')

def about(request):
    return render(request,"user/about.html")

def myevent(request):
    sdata=request.GET.get('search')
    cid=request.GET.get('msg')
    if cid is not None:
        mdata=events.objects.filter(event_name=cid)
    elif sdata is not None:
        mdata=events.objects.filter(Q(event_code__icontains=sdata))
    else:
        mdata=events.objects.all()
    md={"mdata":mdata,}
    return render(request,"user/event.html",md)

def imgallery(request):
    cid=request.GET.get('cid')
    cdata = evnames.objects.all().order_by('-id')
    if cid is not None:
        idata = imgallerys.objects.all().filter(evnames=cid)
    else:
        idata=imgallerys.objects.all().order_by('-id')
    mydict={"idata":idata,"cdata":cdata}
    return render(request,"user/imgallery.html",mydict)

def vigallery(request):
    cid=request.GET.get('x')
    vdata=evnames.objects.all().order_by('-id')
    if cid is not None:
        vdata=vigallerys.objects.filter(evnames=cid)
    else:
        vdata=vigallerys.objects.all().order_by('-id')
        mydict={"vdata":vdata,"vdata":vdata}
    return render(request,"user/vigallery.html",mydict)

def contact(request):
    if request.method =="POST":
        a1=request.POST.get('name')
        a2 = request.POST.get('email')
        a3 = request.POST.get('mobile')
        a4 = request.POST.get('message')
        #print(a1,a2,a3,a4)
        contactus(Name=a1,Email=a2,Mobile=a3,Message=a4).save()
        return HttpResponse("<script> alert('Thank You for Contacting Us ');location.href='/user/contact/'</script>")
    return render(request,"user/contact.html")

def signup(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        passwd=request.POST.get('passwd')
        mobile=request.POST.get('mobile')
        address= request.POST.get('address')
        gender=request.POST.get('gender')
        # picture= request.FILES['fu']
        a=register.objects.filter(email=email).count()
        if a==0:
            register(name=name,email=email,passwd=passwd,mobile=mobile,address=address,gender=gender).save()
            return HttpResponse("<script>alert('You are registered successfully..');location.href='/user/signup'</script>")
            
        else:
            return HttpResponse("<script>alert('You are already registered..');location.href='/user/index/'</script>")
            
    return render(request,"user/signup.html")

def profile(request):
    user=request.session.get('user')
    udata=register.objects.filter(email=user)
    md={"udata":udata}
    if request.method=="POST":
        name=request.POST.get('name')
        mobile=request.POST.get('mobile')
        passwd=request.POST.get('passwd')
        address= request.POST.get('address')
        gender=request.POST.get('gender')
        register(name=name,mobile=mobile,passwd=passwd,gender=gender,address=address,email=user).save()
        return HttpResponse("<script>alert('Your profile is updated successfully..');location.href='/user/myprofile/'</script>")
    return render(request,"user/myprofile.html",md)

def soevent(request):
    sdata=request.GET.get('search')
    cid=request.GET.get('mesg')
    if cid is not None:
        edata=scategory.objects.filter(event_category=cid)
    elif sdata is not None:
        edata=scategory.objects.filter(Q(event_code__icontains=sdata))
    else:
        edata=scategory.objects.all().order_by('-id')
        
    md={"edata":edata,}
    return render(request,"user/soevent.html",md)

def informal(request):
    sdata=request.GET.get('search')
    cid=request.GET.get('mesg')
    if cid is not None:
        idata=incategory.objects.filter(event_category=cid)
    elif sdata is not None:
        idata=incategory.objects.filter(Q(event_code__icontains=sdata))
    else:
        idata=incategory.objects.all().order_by('-id')
    md={"idata":idata,}
    return render(request,"user/informal.html",md)

def charity(request):
    sdata=request.GET.get('search')
    cid=request.GET.get('messg')
    if cid is not None:
        fdata=Ccategory.objects.filter(event_category=cid)
    elif sdata is not None:
        fdata=Ccategory.objects.filter(Q(event_code__icontains=sdata))
    else:
        fdata=Ccategory.objects.all().order_by('-id')
    md={"fdata":fdata,}
    return render(request,"user/charity.html",md)

def education(request):
    sdata=request.GET.get('search')
    cid=request.GET.get('messag')
    if cid is not None:
        eddata=edcategory.objects.filter(event_category=cid)
    elif sdata is not None:
        eddata=edcategory.objects.filter(Q(event_code__icontains=sdata))
    else:
        eddata=edcategory.objects.all().order_by('-id')
    md={"eddata":eddata,}
    return render(request,"user/education.html",md)

def viewdetails(request):
    eid=request.GET.get('msg')
    id=request.GET.get('mssg')
    ind=request.GET.get('mesg')
    edid=request.GET.get('messag')
    edata=scategory.objects.all().filter(id=id)
    mdata=events.objects.all().filter(id=eid)
    idata=incategory.objects.all().filter(id=ind)
    eddata=edcategory.objects.all().filter(id=edid)
    md={"edata":edata,"mdata":mdata,"idata":idata,"eddata":eddata}
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        date=request.POST.get('date')
        price=request.POST.get('price')
        text=request.POST.get('text')
        mobile=request.POST.get('mobile')
        guests=request.POST.get('guests')
        requstprice(name=name,email=email,event_date=date,price=price,text=text,mobile=mobile,no_guests=guests).save()
    return render(request,'user/viewdetails.html',md)


def viewcharity(request):
    fid=request.GET.get('messg')
    fdata=Ccategory.objects.all().filter(id=fid)
    md={"fdata":fdata,}
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        date=request.POST.get('date')
        pan=request.POST.get('pan')
        address=request.POST.get('address')
        mobile=request.POST.get('mobile')
        number=request.POST.get('number')
        Ngo(name=name,email=email,DOB=date,pan_card=pan,address=address,mobile=mobile,utr=number).save()
    return render(request,'user/viewcharity.html',md)

def booking(request):
    user = request.session.get('user')
    if user:
        title = request.GET.get('title')
        epic = request.GET.get('epic')
        place= request.GET.get('place')
        edate = request.GET.get('edate')
        price = request.GET.get('price')
        number=request.GET.get('number')
        
        booknow(userid=user, event_name=title, event_picture=epic, place=place, event_date=edate, event_price=price, no_guests=number,booking_date=datetime.now().date()).save()
        return HttpResponse("<script>alert('Your ticket is booked');location.href='/user/event'</script>")
    return render(request,'user/booking.html')

def mybooking(request):
    bid=request.GET.get('bid')
    user=request.session.get('user')
    ticket="";
    if user:
        ticket=booknow.objects.filter(userid=user)
    if bid is not None:
        ticket=booknow.objects.filter(id=bid).delete()
        return HttpResponse("<script>alert('Your ticket has been canceled..');location.href='/user/mybooking'</script>")
    md={"myticket":ticket}
    return render(request,'user/mybooking.html',md)



