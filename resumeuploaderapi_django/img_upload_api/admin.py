from django.contrib import admin

# Register your models here.
from img_upload_api.models import Profile

# @admin.register(Profile)
class ProfileModelAdmin(admin.ModelAdmin):
    list_display = ['id','name','email','dob','state','gender','loaction','pimage','rdoc']
admin.site.register(Profile)
 