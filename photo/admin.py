from django.contrib import admin

# Register your models here.
from .models import Photo

# 관리자 페이지 커스텀마이징
class PhotoAdmin(admin.ModelAdmin):
    list_display = ['id','author','photo','created']
    ordering = ['-created']

admin.site.register(Photo, PhotoAdmin)