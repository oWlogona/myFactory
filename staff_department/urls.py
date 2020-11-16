from django.urls import path
from staff_department import views

urlpatterns = [
    path("", views.department_list, name="department_list"),
    path("<str:department>/", views.department_detail, name="department_staff"),
]
