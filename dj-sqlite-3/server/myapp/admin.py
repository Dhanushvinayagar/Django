from django.contrib import admin
from .models import Todo

# Register your models here.

admin.site.site_header="Todo admin"


admin.site.register(Todo)