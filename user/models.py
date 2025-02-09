from django.db import models

# Create your models here.

class contactus(models.Model):
    Name = models.CharField(max_length=200,null=True)
    Email=models.CharField(max_length=100,null=True)
    Mobile=models.CharField(max_length=10,null=True)
    Message=models.TextField(null=True)
    def __str__(self):
        return self.Name
    
class evnames(models.Model):
    event_name=models.TextField(max_length=50,null=True) 
    def __str__(self):
        return self.event_name

class feedbacks(models.Model):
    name=models.CharField(max_length=200,null=True)
    email=models.CharField(max_length=100,null=True)
    msg=models.TextField(null=True)
    
class category(models.Model):
    cname=models.CharField(max_length=200,null=True)
    cpic=models.ImageField(upload_to='static/categorypic/',null=True)
    cdate=models.DateField()
    def __str__(self):
        return self.cname
    
class placename(models.Model):
    place=models.CharField(max_length=200,null=True)
    address=models.TextField()
    ppic=models.ImageField(upload_to='static/place/',null=True)
    pdate=models.DateField()
    def __str__(self):
        return self.place    
    
class scategory(models.Model): 
    event_name=models.ForeignKey(evnames,on_delete=models.CASCADE)
    event_place=models.CharField(max_length=200,null=True)
    place=models.CharField(max_length=200,null=True)
    event_code=models.CharField(max_length=20,null=True)
    event_picture=models.ImageField(upload_to='static/Social_Event/',null=True)
    price=models.IntegerField()
    event_date=models.DateField()
    event_detail=models.TextField(null=True)
    no_guests=models.CharField(max_length=100,null=True)
    
class edcategory(models.Model):
    event_name=models.ForeignKey(evnames,on_delete=models.CASCADE)
    speaker_name=models.CharField(max_length=200,null=True)
    event_code=models.CharField(max_length=20,null=True)
    place=models.CharField(max_length=200,null=True)
    event_place=models.CharField(max_length=200,null=True)
    event_picture=models.ImageField(upload_to='static/Education_Event/',null=True)
    price=models.IntegerField()
    event_date=models.DateField()
    event_detail=models.TextField(null=True)
    no_guests=models.CharField(max_length=100,null=True)
    join=models.TextField(null=True)

      

class Ccategory(models.Model):
    event_name=models.ForeignKey(evnames,on_delete=models.CASCADE) 
    NGO_name=models.CharField(max_length=200,null=True)
    event_code=models.CharField(max_length=20,null=True)
    place=models.CharField(max_length=200,null=True)
    city_name=models.CharField(max_length=200,null=True)
    event_picture=models.ImageField(upload_to='static/Charitye_Event/',null=True)
    donation=models.ImageField(upload_to='static/donation/',null=True)
    event_date=models.DateField()
    event_detail=models.TextField(null=True)
       

class incategory(models.Model):
    event_name=models.ForeignKey(evnames,on_delete=models.CASCADE) 
    speaker_name=models.CharField(max_length=200,null=True)
    place=models.CharField(max_length=200,null=True)
    event_code=models.CharField(max_length=20,null=True)
    event_picture=models.ImageField(upload_to='static/Informal_Event/',null=True)
    price=models.IntegerField()
    event_date=models.DateField()
    no_guests=models.CharField(max_length=100,null=True)
    event_detail=models.TextField(null=True)
     
    
class imgallerys(models.Model):
    
    event_name=models.TextField(max_length=100,null=True)
    picture=models.ImageField(upload_to='static/gallery/',null=True)
    event_des=models.TextField(null=True)
    eventdate=models.DateField()

class vigallerys(models.Model):
    
    event_name=models.TextField(max_length=100,null=True)
    vlink=models.TextField(null=True)
    event_des=models.TextField(null=True)
    vdate=models.DateField()    

class slider(models.Model):
    spic=models.ImageField(upload_to='static/slider/',null=True)
    sdate=models.DateField()

class card(models.Model):
    caname=models.CharField(max_length=200,null=True)
    capic=models.ImageField(upload_to='static/card/',null=True)
    cadate=models.DateField()
    cacity=models.CharField(max_length=200,null=True) 
    
class events(models.Model):
    event_name=models.ForeignKey(evnames,on_delete=models.CASCADE) 
    College_name=models.CharField(max_length=200,null=True)
    place=models.CharField(max_length=200,null=True)
    city=models.CharField(max_length=200,null=True)
    event_code=models.CharField(max_length=20,null=True)
    event_picture=models.ImageField(upload_to='static/Event/',null=True)
    no_guests=models.CharField(max_length=100,null=True)
    price=models.IntegerField()
    event_date=models.DateField()
    event_detail=models.TextField(null=True)

class register(models.Model):
    email=models.CharField(max_length=200,primary_key=True)
    name=models.CharField(max_length=200,null=True)
    passwd=models.CharField(max_length=100,null=True)
    gender=models.CharField(max_length=50 ,null=True)
    mobile=models.CharField(max_length=10,null=True)
    address=models.TextField(null=True) 

class booknow(models.Model):
    userid=models.CharField(max_length=200,null=True)
    event_name=models.CharField(max_length=400,null=True)
    event_picture=models.CharField(max_length=400,null=True)
    place=models.CharField(max_length=200,null=True)
    event_date=models.CharField(max_length=100,null=True)
    no_guests=models.CharField(max_length=100,null=True)
    event_price=models.CharField(max_length=200,null=True)
    booking_date=models.DateTimeField()
    
class requstprice(models.Model):
    email=models.CharField(max_length=200,primary_key=True)
    name=models.CharField(max_length=200,null=True)
    price=models.IntegerField()
    event_date=models.DateField()
    mobile=models.CharField(max_length=10,null=True)
    text=models.TextField(null=True)
    no_guests=models.CharField(max_length=100,null=True)

class Ngo(models.Model):
    email=models.CharField(max_length=200,primary_key=True)
    name=models.CharField(max_length=200,null=True)
    mobile=models.CharField(max_length=10,null=True)
    address=models.TextField(null=True)
    pan_card=models.CharField(max_length=200,null=True)
    DOB=models.DateField()
    utr=models.CharField(max_length=200,null=True)
    
        

