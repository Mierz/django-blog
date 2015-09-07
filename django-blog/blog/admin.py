from django.contrib import admin

# Register your models here.
from .models import Post, Categorie, Page

admin.site.register(Post)
admin.site.register(Categorie)
admin.site.register(Page)