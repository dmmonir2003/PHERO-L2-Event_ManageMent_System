# from django.contrib import admin
# from .models import User
# from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


# class UserModelAdmin(BaseUserAdmin):

#     list_display = ('id', 'email', 'name', 'role', 'is_superuser')
#     list_filter = ('is_superuser', 'id',)
#     list_editable = ('role',)
#     fieldsets = (
#         ('User Credentials', {'fields': ('email', 'password',)}),
#         ('Personal info', {'fields': ('name', 'role',)}),
#         ('Permissions', {'fields': ('is_superuser',)}),
#     )

#     add_fieldsets = (
#         (None, {
#             'classes': ('wide',),
#             'fields': ('email', 'name', 'role', 'password1', 'password2',),
#         }),
#     )
#     search_fields = ('email',)
#     ordering = ('email', 'id',)
#     filter_horizontal = ()


# admin.site.register(User, UserModelAdmin)
