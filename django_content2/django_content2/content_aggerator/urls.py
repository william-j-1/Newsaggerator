
from django.urls import path
from . import views
urlpatterns = [
    path('', views.home,name='aggerator-home'),
    path('about/',views.about,name='aggerator-about'),
    #path('search/',views.search,name='aggerator-search'),
    path('log-in/',views.send),
    path('create-account/',views.create_account),
    path('create-account/submit',views.submit),
    path('log-in/submit',views.login),

]