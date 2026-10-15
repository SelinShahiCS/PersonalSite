from django.contrib import admin
from .models import Article


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ("title" , "created_at")
    search_fields  = ("title" , "description" , "content")
    ordering = ("-created_at" ,)
    prepopulated_fields =  {"slug": ("title",)}
    list_filter = ("created_at" ,)
