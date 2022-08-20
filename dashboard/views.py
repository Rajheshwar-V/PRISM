from http import HTTPStatus
from sre_constants import SUCCESS
from telnetlib import STATUS
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from .models import *
# Create your views here.

import base64

from django.core.files.base import ContentFile

def main_dashboard(request):

    return render(request, 'dashboard/index.html')


def save_study(request):
    if request.method == "POST":
        # print(request.POST)
        # print(request.FILES)
        name1 =  request.POST["name1"]
        type1 = request.POST["type1"]
        comment = request.POST["comments"]
        image1 = request.FILES["image1"]

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

    study_images = StudyImages.objects.filter(study_id=study_id)

    return render(request, 'dashboard/report.html', context={
        "study": study, "study_images":study_images
    })

