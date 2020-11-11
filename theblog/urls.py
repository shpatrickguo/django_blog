from django.urls import path
<<<<<<< HEAD
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
=======
from .views import HomeView

urlpatterns = [
    path('', HomeView,as_view(), name="home"),
>>>>>>> parent of 471f4b3... homeview
]
