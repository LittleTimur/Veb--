from django.db import models
from django.conf import settings
import uuid

# Модель профиля

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) #1
    # Дополнительные поля
    name = models.CharField(max_length=30, blank=True)  #2
    surname = models.CharField(max_length=30, blank=True) #3
    bio = models.TextField(max_length=500, blank=True)   #4
    location = models.CharField(max_length=30, blank=True)  #5
    birth_date = models.DateField(null=True, blank=True)   #6
    img = models.ImageField(upload_to='images/', null=True, default='needimages/defaultimage.png')   #7
    verification_token = models.UUIDField(default=uuid.uuid4, editable=False)   #8
    is_verified = models.BooleanField(default=False)   #9

class Cate(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name
#модель для объвления
class announmodel(models.Model):
    about=models.CharField(max_length=100,default='Описание отсутствует')   #1
    name = models.CharField(max_length=30)   #2
    img = models.ImageField(upload_to='images/', null=True)   #3
    value = models.IntegerField()   #4
    id_account = models.ForeignKey(Profile, on_delete=models.CASCADE)   #5
    id_announ = models.AutoField(primary_key=True)   #6
    announ_cat = models.ForeignKey(Cate, on_delete=models.CASCADE)   #7

class Message(models.Model):
    sender = models.ForeignKey(
        Profile, on_delete=models.SET_NULL, null=True, blank=True)
    recipient = models.ForeignKey(
        Profile, on_delete=models.SET_NULL, null=True, blank=True, related_name="messages")
    name = models.CharField(max_length=200, null=True, blank=True)
    surname = models.CharField(max_length=200, null=True, blank=True)
    subject = models.CharField(max_length=200, null=True, blank=True)
    body = models.TextField()
    is_read = models.BooleanField(default=False, null=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return self.subject

    class Meta:
        ordering = ['is_read', '-created']