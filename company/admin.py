from django.contrib import admin
from . import models
# Register your models here.
class companyAdmin(admin.ModelAdmin):
    pass

admin.site.register(models.Company, companyAdmin)