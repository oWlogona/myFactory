from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from staff_department.models import UserSpecialty, Profile
from staff_department.forms import ProfileForm, UserSpecialtyForm


def department_list(request):
    if request.method == 'POST':
        form = UserSpecialtyForm(request.POST)
        specialty_name = form.data.get('name')
        UserSpecialty.objects.create(name=specialty_name)
        return HttpResponseRedirect('/departments/')

    form = UserSpecialtyForm()
    specialties = UserSpecialty.objects.all()
    response = {specialty.name: specialty.profile_set.all() for specialty in specialties}
    return render(request, 'staff_department/department_list.html', locals())


def department_detail(request, department):
    department = UserSpecialty.objects.filter(name=department).first()
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        data = form.data
        Profile.objects.create(first_name=data.get('first_name'), last_name=data.get('last_name'),
                               gender=data.get('gender'), age=data.get('age'), specialty=department)
        return HttpResponseRedirect(f'/departments/{department}')

    form = ProfileForm()
    response = {'name': department.name, 'staff': department.profile_set.all()}
    return render(request, 'staff_department/department_staff.html', locals())
