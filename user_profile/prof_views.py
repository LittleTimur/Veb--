from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm
from our_models import views

@login_required
def user_profile(request):
    user = request.user
    about_user = views.Get_Profile_by_user(request.user)
    announs = views.Announmodel_Get_All().filter(id_account=about_user.id)
    return render(request,'user_profile/user_profile.html',{'email': user.email, 'announs':announs, 'about_user':about_user})


def owner_profile(request, id):
    announ = views.Announmodel_Get(id)
    about_user = announ.id_account
    print(about_user.user.email)
    announs = views.Announmodel_Get_All().filter(id_account=about_user)
    if request.user.is_authenticated and request.user == about_user.user:
        return HttpResponseRedirect(reverse("user_profile"))
    return render(request,'user_profile/owner_profile.html',{'announs':announs, 'about_user':about_user})

@login_required
def change_profile(request):
    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            # Предполагаем, что у вас есть модель Profile с полями, соответствующими полям формы
            profile = views.Get_Profile_by_user(request.user)  # Получаем профиль текущего пользователя
            profile.name = form.cleaned_data['name']
            profile.surname = form.cleaned_data['surname']
            profile.bio = form.cleaned_data['bio']
            profile.location = form.cleaned_data['location']
            profile.birth_date = form.cleaned_data['birth_date']
            if 'img' in request.FILES:
                profile.img = request.FILES['img']
            profile.save()  # Сохраняем изменения в базе данных
        return HttpResponseRedirect(reverse("user_profile"))
    else:
        profile = views.Get_Profile_by_user(request.user)  # Получаем профиль текущего пользователя
        fp = ProfileForm()
        return render(request, "user_profile/profile_change.html", {"form": fp,"about_user":profile})

