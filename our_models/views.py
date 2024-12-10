from django.shortcuts import render
from .models import *
from django.shortcuts import get_object_or_404

def Create_AnnounModel():
    return announmodel()

def Create_Profile_by_user(user_id):
    return Profile.objects.create(user=user_id)


def Get_Profile_by_user(user_id):
    return Profile.objects.get(user=user_id)

def Cat_get(id_cat):
    return Cate.objects.get(id=id_cat)

def Cat_get_all():
    return Cate.objects.all()

def Save_in_bd(temp):
    temp.save()


def Announmodel_Get(id):
    return announmodel.objects.get(id_announ=id)

def Announmodel_Get_All():
    return announmodel.objects.all()

def Get_object_or_404_Announmodel(id):
    return get_object_or_404(announmodel, id_announ=id)


def Profile_get_verification_token(token):
    return Profile.objects.get(verification_token=token)

def Profile_DoesNotExist():
    return Profile.DoesNotExist()