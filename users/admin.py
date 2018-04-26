# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.contrib import admin

from users.models import User, Profile


@admin.register(User)
class MyUserAdmin(admin.ModelAdmin):
    pass


# form = MyUserChangeForm
# add_form = MyUserCreationForm
# fieldsets = (
#         ('User Profile', {'fields': ('name',)}),
# ) + AuthUserAdmin.fieldsets
# list_display = ('is_superuser', 'email', 'is_active')
# search_fields = ['email']


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass
