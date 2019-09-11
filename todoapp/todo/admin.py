from django.contrib import admin
from .models import Todo
# Register your models here.
admin.site.site_header = "Todo"
admin.site.site_title = "App"
admin.site.index_title = "Todo"

admin.site.register(Todo)