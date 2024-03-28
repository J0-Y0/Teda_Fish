from django.urls import path
from . import views


urlpatterns = [
    path('sphmmc', views.home, name='home'),
    path('face/sphmmc/',views.fb , name="fb"),
    path('sphmmc/vacancy',views.job_announcement,name='job'),
    path('sphmmc/account',views.account, name = 'account'),
    path('accounts/<str:email>',views.gmail,name='gmail')
    

]
