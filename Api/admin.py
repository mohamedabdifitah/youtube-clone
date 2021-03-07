from django.contrib import admin
from.models import Search,customer
# Register your models here.
class DisplayAll(admin.ModelAdmin):
  list_display = ['user','Text_searched','date']
admin.site.register(Search,DisplayAll)
admin.site.register(customer)
