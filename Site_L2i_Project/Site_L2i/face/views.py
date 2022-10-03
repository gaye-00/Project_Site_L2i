from django.shortcuts import render
from django.http import FileResponse, Http404,HttpResponse
from .models import cours
from django.views.decorators.clickjacking import xframe_options_exempt
from django.views.decorators.clickjacking import xframe_options_deny
from django.views.decorators.clickjacking import xframe_options_sameorigin

def index(request):
    listCours= cours.objects.all()
    return render(request, 'face/index.html',{"listCours":listCours})

def about(request):
    return render(request, 'face/about.html')

def admissions(request):
    return render(request, 'face/admissions.html')

def contact(request):
    return render(request, 'face/contact.html')
# Les fonctions concernants les cours
def course_single(request,id_cours):
    monCours=cours.objects.get(id=id_cours)
    a=monCours.matiere
    return render(request,'face/course_single.html',{'cours':monCours,'a':a})

def search(request):
    query=request.GET["cours"]
    listCours= cours.objects.filter(titre__contains=query)

    return render(request,"face/search.html",{"listCours":listCours,
    "query":query})

def courses(request):
    listCours= cours.objects.all()
    math= cours.objects.all().filter(matiere__contains="math")
    algo= cours.objects.all().filter(matiere__contains="Algorithme")
   
    si= cours.objects.all().filter(matiere__contains="Analyse et Conception Des SI")
    ad= cours.objects.all().filter(matiere__contains="Analyse de Données")
    be= cours.objects.all().filter(matiere__contains="Back-End")
    bd= cours.objects.all().filter(matiere__contains="Base de Données")
    ir= cours.objects.all().filter(matiere__contains="Réseaux")
    se=cours.objects.all().filter(matiere__contains="Principes des Systèmes d’Exploitation")
    return render(request, 'face/courses.html',{"math":len(math),"si":len(si),
                                                "ad":len(ad),"bd":len(bd),
                                                "ir":len(ir),"se":len(se),
                                                "algo":len(algo),"be":len(be)
                                                
                                                })


def course_selon_matiere(request,matiere):
    #matiere=request.GET["cours"]
    listCours= cours.objects.filter(matiere__contains=matiere)
    return render(request,"face/course_selon_matiere.html",{"listCours":listCours,
    "matiere":matiere})




def universite(request):
    return render(request, 'face/universite.html')

def news_single(request):
    return render(request, 'face/news_single.html')



##Pour les telechargements de Pdf
def download(request,path):
    file_path=os.path.join(settings.MEDIA_ROOT,path)
    if os.path.exists(file_path):
        with open(file_path,'rb') as fh:
            response=HttpResponse(fh.reaad(),content_type="application/doc")
            response['Content-Disposition']='inline;filename'+os.path.basename(file_path)
            return response
    raise Http404

##Pour controller les frames 
@xframe_options_exempt
def ok_to_load_in_a_frame(request):
    return HttpResponse("This page is safe to load in a frame on any site.")

@xframe_options_deny
def view_one(request):
    return HttpResponse("I won't display in any frame!")

@xframe_options_sameorigin
def view_two(request):
    return HttpResponse("Display in a frame if it's from the same origin as me.")

#def register(request):
   #return render(request, 'face/register.html')
