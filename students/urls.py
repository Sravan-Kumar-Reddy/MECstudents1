from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    #path('<Student_id>',views.cgpa,name = 'cgpa'),
]