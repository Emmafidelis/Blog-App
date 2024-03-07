from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
  list_display = ['title', 'date_posted', 'author']

# Register your models here.
