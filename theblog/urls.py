from django.urls import path
<<<<<<< HEAD
<<<<<<< HEAD
from .views import Home

urlpatterns = [
    path('', Home,as_view(), name="home"),
=======
from . import views

urlpatterns = [
    path('', views.home, name="home")
>>>>>>> parent of 01ff698... 2
=======
from . import views

urlpatterns = [
    path('', views.home, name="home")
>>>>>>> parent of 01ff698... 2
]
