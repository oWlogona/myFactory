from django.contrib import admin
from staff_department.models import Profile, UserSpecialty


class ProfileAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Profile._meta.fields]


class UserSpecialtyAdmin(admin.ModelAdmin):
    list_display = [field.name for field in UserSpecialty._meta.fields]


admin.site.register(Profile, ProfileAdmin)
admin.site.register(UserSpecialty, UserSpecialtyAdmin)
