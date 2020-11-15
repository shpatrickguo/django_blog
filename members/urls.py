from django.urls import path
from .views import UserRegisterView, UserEditView, PasswordsChangeView, ShowProfilePageView, EditProfilePageView
from . import views

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name="register"),
    path('edit_profile/', UserEditView.as_view(), name="edit_profile"),
    path('password/', PasswordsChangeView.as_view()),
    path('password_sucess/', views.password_success, name="password_success"),
    path('<int:pk>/profile/', ShowProfilePageView.as_view(), name="show_profile_page"),
    path('<int:pk>/edit_profile_page/', EditProfilePageView.as_view(), name="edit_profile_page"),
]
