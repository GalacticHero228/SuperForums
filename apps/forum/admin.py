from django.contrib import admin

# Register your models here.
from apps.forum.models import *

admin.site.register(Topic)
admin.site.register(Entry)
admin.site.register(Category)