from django.contrib import admin

# Register your models here.
from forum.models import *

admin.site.register(Topic)
admin.site.register(Entry)
admin.site.register(Category)