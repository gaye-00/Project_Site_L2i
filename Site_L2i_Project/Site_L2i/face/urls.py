from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('about/', views.about, name='about'),
   
    path('admissions/', views.admissions, name='admissions'),
    path('contact/', views.contact, name='contact'),
    path('course_single/<int:id_cours>', views.course_single, name='course_single'),
    path('courses/', views.courses, name='courses'),
    path('universite/', views.universite, name='universite'),
    path('search/', views.search, name='search'),
    path('course_selon_matiere/<str:matiere>', views.course_selon_matiere, name='course_selon_matiere'),
   
    #path('login/', views.login, name='login'),
    path('news_single/', views.news_single, name='news_single'),
    #path('register/', views.register, name='register'),
]