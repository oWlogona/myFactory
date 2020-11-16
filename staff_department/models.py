from django.contrib.auth.models import User
from django.db import models


class UserSpecialty(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name


class Profile(models.Model):
    class ProfileGender:
        male = "male"
        female = "female"

    ProfileGenderChoice = (
        (ProfileGender.male, "male"),
        (ProfileGender.female, "female"),
    )

    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    gender = models.CharField(verbose_name="gender", max_length=10, default=ProfileGender.male)
    age = models.IntegerField(default=1)
    specialty = models.ForeignKey(verbose_name="specialty", to="UserSpecialty", null=True, blank=True,
                                  on_delete=models.SET_NULL)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
