import uuid
from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseRedirect
from announproject.settings import EMAIL_HOST_USER
from .forms import announForm
from user_profile.forms import ProfileForm
from our_models import views
import os
from django.conf import settings
from django.urls import reverse
from django.contrib.auth.decorators import login_required

def main(request):
    return HttpResponseRedirect("/SRAST")

def SRAST(request):
    announcements = views.Announmodel_Get_All()
    categories = views.Cat_get_all()
    return render(request, 'SRAST.html', {'announcements': announcements, 'categories': categories})

@login_required
def announcreate(request):
    profile = views.Get_Profile_by_user(request.user)
    if profile.is_verified:
        if request.method == "POST":
            # Получение данных из запроса
            am=views.Create_AnnounModel()
            am.name = request.POST.get('name')
            am.about=request.POST.get('about')
            am.img = request.FILES.get('img')
            am.value = request.POST.get('value')
            am.announ_cat = views.Cat_get(request.POST.get('cat'))
            #загоняем данные в модель для сохранения в бд
            #нужно прикрутить получение айди юзера
            am.id_account = views.Get_Profile_by_user(request.user)
            views.Save_in_bd(am)

            return HttpResponseRedirect(reverse('announshow', args=(am.id_announ,)))
        else:
            uf = announForm()
            return render(request, "announ/announcreate.html", {"form": uf})
    else:
        return render(request,'announ/atemption.html')
    
def announshow(request,id):
    an = views.Get_object_or_404_Announmodel(id)
    pathtoimg = settings.MEDIA_URL + str(an.img)
    related_announs = views.Announmodel_Get_All().filter(announ_cat=an.announ_cat).exclude(id_announ=an.id_announ)
    user_about = an.id_account
    return render(request,"announ/announshow.html",{"announ":an,"related_announs1":related_announs[0:2],"related_announs2":related_announs[2:4], "user_about":user_about})


def allannoun(request):
     # Получаем все объекты модели AnnounModel
    announs = views.Announmodel_Get_All()
    return render(request, 'announ/allannoun.html',  {'announs': announs})


def category_detail (request, category_id):
    announs = views.Announmodel_Get_All().filter(announ_cat__id = category_id)
    category = views.Cat_get(category_id)
    announ_count = announs.count()
    return render(request, 'announ/category_detail.html', {'announs': announs, 'category': category, 'announ_count':announ_count})

