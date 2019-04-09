from django.shortcuts import render,render_to_response
from django.http import HttpResponse
from django.template import loader
from .models import *
#import requests

# Create your views here.

def index(request):
    student_entries = Students.objects.all()
    course_entries = Courses.objects.all()
    instructor_entries = Instructors.objects.all()
    Grade_entries = Grades.objects.all()

    template = loader.get_template('students/index.html')
    context = {
        'students_entries' : student_entries,
        'courses_entries' : course_entries,
        'instructors_entries' : instructor_entries
    }
    return HttpResponse(template.render(context,request))

def cgpa(Student_id):
    print ('Hello i am here!')
    return 0
