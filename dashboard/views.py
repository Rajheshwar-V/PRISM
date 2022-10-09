from http import HTTPStatus
from sre_constants import SUCCESS
from telnetlib import STATUS
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render, reverse
from .models import *
# Create your views here.

import os
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.conf import settings
import base64


def main_dashboard(request):
    global file
    
    if request.method == "POST":
        print(request.POST)
        print(request.FILES)

        comment = request.POST["w3review"]
        title = request.POST["title"]
        
        new_study1 = Study(study_name=title, comment=comment)
        new_study1.save()
        
        print(file)
        image = None


        name1 =  request.POST["name1"]
        type1 = request.POST["type1"]
        img1highlight = request.POST.get('img1highlight', False)
        color1 = request.POST["color1"]
        new_study_image1 = StudyImages(device=name1, photo_type=type1, image=image, highlight=img1highlight, color=color1, study_id=new_study1)
        new_study_image1.save()
        image = open(file, 'rb').read()
        new_study_image1.image.save('image1.jpg', ContentFile(image))

        original = new_study_image1.image.open()

        name2 =  request.POST["name2"]
        type2 = request.POST["type2"]
        img2highlight = request.POST.get('img2highlight', False)
        color2 = request.POST["color2"]
        
        # new_study2 = Study(study_name=study_name, comment=comment)
        # new_study2.save()
        new_study_image2 = StudyImages(device=name2, photo_type=type2, image=original, highlight=img2highlight, color=color2, study_id=new_study1)
        new_study_image2.save()



        name3 =  request.POST["name3"]
        type3 = request.POST["type3"]
        img3highlight = request.POST.get('img3highlight', False)
        color3 = request.POST["color3"]

        # new_study3 = Study(study_name=study_name, comment=comment)
        # new_study3.save()

        new_study_image3 = StudyImages(device=name3, photo_type=type3, image=original, highlight=img3highlight, color=color3, study_id=new_study1)
        new_study_image3.save()
        return redirect(reverse("home"))

    return render(request, 'dashboard/index.html')



file = None

def save_study(request):
    global file

    if request.method == "POST":
        print(request.POST)
        print(request.FILES)
        print("from save_study")

        comment = request.POST["comments"]
        name1 =  request.POST["name1"]
        type1 = request.POST["type1"]
        image1 = request.FILES["image1"]

        image_name = image1.name
        print(image_name)
        path = default_storage.save(f'tmp/{image_name}', ContentFile(image1.read()))
        file = os.path.join(settings.MEDIA_ROOT, path)

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

        # new_study = Study(study_name=study_name, comment=comment)
        # new_study.save()

        # new_study_image = StudyImages(device=name1, photo_type=type1, image=image1, study_id=new_study)
        # new_study_image.save()

        return JsonResponse({'status':'200', "value": "21323"})

    return JsonResponse({'link':'/dashboard'})


def all_studies(request):
    studies = Study.objects.all()
    return render(request, 'dashboard/reportlist.html', context={
        "studies": studies
    })


def view_study_list(request):
    if request.method == "POST":
        report_list = request.POST.getlist('report_list')
        # print(report_list)

        study_sets = {}
        for study_id in report_list:
            study = Study.objects.filter(study_id=study_id)[0]
            print(study)
            study_sets[study] = StudyImages.objects.filter(study_id=study_id)
        return render(request, 'dashboard/view_report_list.html', {
            "study_sets": study_sets,
        })


def view_study(request, study_id):
    study = Study.objects.filter(study_id=study_id)[0]
    study_images = StudyImages.objects.filter(study_id=study_id)
    
    return render(request, 'dashboard/report.html', context={
        "study": study, 
        "study_images":study_images,
    })

