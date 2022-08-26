from http import HTTPStatus
from sre_constants import SUCCESS
from telnetlib import STATUS
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render, reverse
from .models import *
# Create your views here.

import base64

from django.core.files.base import ContentFile

hig_color = None

def main_dashboard(request):
    if request.method == "POST":
        print(request.POST)
        print(request.FILES)

        comment = request.POST["w3review"]
        global hig_color 
        hig_color = request.POST["color1"]

        name1 =  request.POST["name1"]
        type1 = request.POST["type1"]
        image1 = request.FILES.get("image1", False)
        study_name = name1
        new_study = Study(study_name=study_name, comment=comment)
        new_study.save()
        new_study_image1 = StudyImages(device=name1, photo_type=type1, image=image1, study_id=new_study)
        new_study_image1.save()


        name2 =  request.POST["name2"]
        type2 = request.POST["type2"]
        image2 = request.FILES.get("image2", False)
        study_name = name2
        new_study = Study(study_name=study_name, comment=comment)
        new_study.save()
        new_study_image2 = StudyImages(device=name2, photo_type=type2, image=image2, study_id=new_study)
        new_study_image2.save()



        name3 =  request.POST["name3"]
        type3 = request.POST["type3"]
        image3 = request.FILES.get("image3", False)
        study_name = name3

        new_study = Study(study_name=study_name, comment=comment)
        new_study.save()

        new_study_image3 = StudyImages(device=name3, photo_type=type3, image=image3, study_id=new_study)
        new_study_image3.save()
        return redirect(reverse("home"))
    return render(request, 'dashboard/index.html')


def save_study(request):
    if request.method == "POST":
        print(request.POST)
        print(request.FILES)
        print("from save_study")

        comment = request.POST["comments"]
        name1 =  request.POST["name1"]
        type1 = request.POST["type1"]
        image1 = request.FILES["image1"]

        # name2 =  request.POST.get('name2', False)
        # type2 = request.POST["type2"]
        # comment = request.POST["comments"]
        # image2 = request.FILES["image2"]

        # name3 =  request.POST.get('name3', False)
        # type3 = request.POST["type3"]
        # comment = request.POST["comments"]
        # image3 = request.FILES["image3"]

        
        # image1_base64 = request.POST["image1"]

        # format, imgstr = image1_base64.split(';base64,') 
        # ext = format.split('/')[-1] 

        # image1 = ContentFile(base64.b64decode(imgstr), name='temp.' + ext)

        # print(image1)

        study_name = name1

        new_study = Study(study_name=study_name, comment=comment)
        new_study.save()

        new_study_image1 = StudyImages(device=name1, photo_type=type1, image=image1, study_id=new_study)
        new_study_image1.save()

        return JsonResponse({'status':'200', "value": "21323"})

    return JsonResponse({'link':'/dashboard'})


def all_studies(request):
    studies = Study.objects.all()
    return render(request, 'dashboard/reportlist.html', context={
        "studies": studies
    })


def view_study(request, study_id):
    study = Study.objects.filter(study_id=study_id)[0]
    global hig_color
    study_images = StudyImages.objects.filter(study_id=study_id)
    
    print("col", hig_color)
    return render(request, 'dashboard/report.html', context={
        "study": study, 
        "study_images":study_images,
        "color1": hig_color,
    })

