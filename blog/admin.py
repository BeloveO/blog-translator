from django.contrib import admin
from .models import Post, Comment, Tag
from django.contrib.auth.admin import UserAdmin 

class PostAdmin(admin.ModelAdmin):
    list_display= ('title', 'date_created', 'author')
    list_filter = ("status",)
    search_fields = ['title', 'content', 'author']
    # this creates the slug field from the title field
    prepopulated_fields = {'slug': ('title',)}
    autocomplete_fields = ('tags',)


class TagAdmin(admin.ModelAdmin):
    search_fields = ('name',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'post', 'created_on', 'active')
    list_filter = ('active', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)


# Register your models here.
admin.site.register(Post, PostAdmin)
admin.site.register(Tag, TagAdmin)

