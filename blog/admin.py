from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from .models import Post

admin.site.register(Post)
admin.site.register(CustomUser, UserAdmin)