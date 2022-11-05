from django.contrib import admin

from blog.models import Profile, Post, Tag


# Register your models here.
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    model = Profile
