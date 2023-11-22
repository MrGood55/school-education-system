from django.contrib import admin

from .models import *
# Register your models here.



admin.site.register(School)

@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('first_name','middle_name','last_name','school','status','address')



admin.site.register(Subject)
admin.site.register(Group)
# @admin.register(School)
# class PersonAdmin(ImportExportModelAdmin):
#     list_display = '__all__'