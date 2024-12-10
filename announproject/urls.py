
from django.contrib import admin
from announ import views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from user_profile import prof_views
from chat import chat_views

from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.main, name='home'),
    path('SRAST/', views.SRAST, name='SRAST'),
    path('SRAST/createannoun/',views.announcreate,name='announcreate'),
    path('SRAST/announs/id=<int:id>',views.announshow,name='announshow'),
    path('SRAST/announs/', views.allannoun, name='announlist'),
    path('SRAST/profile/', prof_views.user_profile, name='user_profile'),
     path('SRAST/profile/change', prof_views.change_profile, name='changeprofile'),
    path('SRAST/category/<int:category_id>/', views.category_detail, name='category'),
    path('SRAST/announs/id=<int:id>/profile',prof_views.owner_profile,name='owner_profile'),
    path('accounts/', include('registration.urls')),
     path('SRAST/inbox/', chat_views.inbox, name="inbox"),
    path('SRAST/message/<str:pk>/', chat_views.viewMessage, name="message"),
    path('SRAST/create-message/<int:user_id>/', chat_views.createMessage, name="create-message"),
   # path('', TemplateView.as_view(template_name="index.html"), name='home'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
