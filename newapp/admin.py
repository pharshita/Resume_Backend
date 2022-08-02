from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.admin import UserAdmin
from .models import User
from django.contrib import admin
from .models import *

class UserAdmin(BaseUserAdmin):
    fieldsets = (
        (None, {'fields': ('email', 'password', )}),
        (_('Personal info'), {'fields': ('first_name', 'last_name')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser','groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
        # (_('user_info'), {'fields': ('native_name', 'phone_no')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide', ),
            'fields': ('email', 'password1', 'password2'),
        }),
    )
    list_display = ['email', 'first_name', 'last_name', 'is_staff']
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('email', )
admin.site.register(User, UserAdmin)




# Register your models here.
admin.site.register(ExperienceModel)
admin.site.register(EducationModel)
admin.site.register(SkillsModel)

class ExperienceAdmin(admin.StackedInline):
    model = ExperienceModel

class EducationModelAdmin(admin.StackedInline):
    model = EducationModel

class UserAdmin(admin.ModelAdmin):
    model = UserInformations
    inlines = [ExperienceAdmin,EducationModelAdmin]

admin.site.register(UserInformations,UserAdmin)

admin.site.register(Jobapplication)
admin.site.register(Job)