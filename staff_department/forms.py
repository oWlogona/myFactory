from django.forms import ModelForm

from staff_department.models import Profile, UserSpecialty


class UserSpecialtyForm(ModelForm):
    class Meta:
        model = UserSpecialty
        fields = "__all__"


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'gender', 'age']
