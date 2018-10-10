from django.urls import path
from Database.views import *

urlpatterns = [
    path('', student_list, name='Student_list'),
    path('<int:id>/details/', student_details, name='Student_detail'),
    path('<int:id>/edit/', student_edit, name="Student_edit"),
    path('<int:id>/delete/', student_delete, name="Student_delete"),
    path('add/', student_add, name="Student_add"),
    path('search/', student_search, name="Student_search"),
]