from django.contrib import admin
from.models import service_req

# Register your models here.

class hm_admin(admin.ModelAdmin):
    list_display = ['name','email_id','country_code','mobile_no','service_type','service_info']

admin.site.register(service_req,hm_admin)