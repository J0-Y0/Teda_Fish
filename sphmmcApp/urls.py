from django.urls import path
from . import views


urlpatterns = [
    path('sphmmc.edu.et', views.home, name='home'),
    path('facebook.com/sphmmc/',views.fb , name="fb"),
    path('sphmmc.edu.et/vacancy',views.job_announcement,name='job'),
    path('sphmmc.edu.et/account',views.account, name = 'account'),
    path('accounts.google.com/<str:email>',views.gmail,name='gmail')
    

]
