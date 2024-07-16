from django.urls import path
from loginapp import views

urlpatterns = [
    path('',views.homePage),
    path('login/',views.login),
    path('signup/',views.signup),

]
