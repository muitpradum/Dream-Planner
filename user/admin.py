from django.contrib import admin
from . models import *
# Register your models here.
class contactusAdmin(admin.ModelAdmin):
    list_display = ('Name','Email','Mobile','Message')
admin.site.register(contactus,contactusAdmin)

class evnamesAdmin(admin.ModelAdmin):
    list_display=('id','event_name',)
admin.site.register(evnames,evnamesAdmin)

class placenameAdmin(admin.ModelAdmin):
    list_display = ('id','place','address','ppic','pdate')
admin.site.register(placename,placenameAdmin)

class categoryAdmin(admin.ModelAdmin):
    list_display = ('id','cname','cpic','cdate')
admin.site.register(category,categoryAdmin)

class sliderAdmin(admin.ModelAdmin):
    list_display = ('id','spic','sdate')
admin.site.register(slider,sliderAdmin)

class cardAdmin(admin.ModelAdmin):
    list_display = ('id','capic','cadate','caname','cacity')
admin.site.register(card,cardAdmin)

class registerAdmin(admin.ModelAdmin):
    list_display=('email','passwd','name','mobile','address','gender')
admin.site.register(register,registerAdmin)

class feedbacksAdmin(admin.ModelAdmin):
    list_display=('id','name','email','msg')
admin.site.register(feedbacks,feedbacksAdmin)  

class scategoryAdmin(admin.ModelAdmin):
    list_display =('id','event_name','event_code','event_place','place','event_picture','price','event_date','event_detail','no_guests')
admin.site.register(scategory,scategoryAdmin)

class edcategoryAdmin(admin.ModelAdmin):
    list_display =('id','event_name','event_code', 'speaker_name','place','event_picture','price','event_date','event_detail','no_guests','event_place','join')
admin.site.register(edcategory,edcategoryAdmin)

class incategoryAdmin(admin.ModelAdmin):
    list_display =('id','event_name','event_code', 'speaker_name','place','event_picture','price','event_date','event_detail','no_guests')
admin.site.register(incategory,incategoryAdmin)

class CcategoryAdmin(admin.ModelAdmin):
    list_display =('id','event_name','event_code','NGO_name','place','event_picture','donation','event_date','event_detail',)
admin.site.register(Ccategory,CcategoryAdmin)

class imgallerysAdmin(admin.ModelAdmin):
    list_display = ('id','picture','event_name','eventdate','event_des')
admin.site.register(imgallerys,imgallerysAdmin)

class vigallerysAdmin(admin.ModelAdmin):
    list_display = ('id','vlink','vdate','event_des','event_name')
admin.site.register(vigallerys,vigallerysAdmin)

class eventsAdmin(admin.ModelAdmin):
    list_display = ('id','event_name','event_code','place','city', 'event_picture','price','event_date','event_detail','College_name','no_guests')
admin.site.register(events,eventsAdmin)

class booknowAdmin(admin.ModelAdmin):
    list_display=('id','userid','event_name','event_picture','event_date','event_price','booking_date','no_guests')
admin.site.register(booknow,booknowAdmin)

class requstpriceAdmin(admin.ModelAdmin):
    list_display=('email','price','name','mobile','text','event_date','no_guests')
admin.site.register(requstprice,requstpriceAdmin)  

class NgoAdmin(admin.ModelAdmin):
    list_display=('email','name','mobile','address','DOB','pan_card','utr')
admin.site.register(Ngo,NgoAdmin)    

   
