from django.contrib import admin
from .models import Person, TeleVision, Mobile, Company
# Register your models here.

class PersonAdmin(admin.ModelAdmin):
    model = Person

class TelevisionAdmin(admin.ModelAdmin):
    model = TeleVision
    list_display = ['company', 'model', 'price']
    list_filter = ['company', 'model']

admin.site.register(Person, PersonAdmin)
admin.site.register(TeleVision, TelevisionAdmin)
admin.site.register(Mobile)
admin.site.register(Company)

