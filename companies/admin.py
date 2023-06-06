from django.contrib import admin
from . import models
# Register your models here.
class companyAdmin(admin.ModelAdmin):
    list_display = ('title',)
    filter_horizontal = ('languages',)  # Use filter_horizontal for a more user-friendly display

admin.site.register(models.Language)
admin.site.register(models.Companies, companyAdmin)