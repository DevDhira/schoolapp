from django.shortcuts import render
from django.views.generic import ListView

from app.models import Student


# Create your views here.

class StudentList(ListView):
    model = Student

    