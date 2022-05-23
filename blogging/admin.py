from django.contrib import admin

# Register your models here.
from blogging.models import Post, Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    exclude = ['posts']


class CategoryInline(admin.TabularInline):
    model = Category.posts.through


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    model = Post
    inlines = [
        CategoryInline,
    ]

# admin.site.register(Post)
# admin.site.register(Category)