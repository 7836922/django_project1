from django.contrib import admin

from app1 import models
from .models import trainer



# Register your models here.
class TrainerAdmin(admin.ModelAdmin):
    list_display=('name','location','email','phone','technology1','technology2')
admin.site.register(trainer,TrainerAdmin)