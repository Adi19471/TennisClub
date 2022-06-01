from django.contrib import admin

# Register your models here.
from .models import Book_ground,Contact

admin.site.register(Contact)
admin.site.register(Book_ground)
