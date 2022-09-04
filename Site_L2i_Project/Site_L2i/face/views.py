from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'face/index.html')

def about(request):
    return render(request, 'face/about.html')

def admissions(request):
    return render(request, 'face/admissions.html')

def contact(request):
    return render(request, 'face/contact.html')

def course_single(request):
    return render(request, 'face/course-single.html')

def courses(request):
    return render(request, 'face/courses.html')

#def login(request):
    #return render(request, 'face/login.html')

def news_single(request):
    return render(request, 'face/news-single.html')

#def register(request):
   #return render(request, 'face/register.html')