from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
# from authy.views import UserProfile, EditProfile
app_name ='profiles'

urlpatterns = [
    # Profile Section
    # path('profile/edit', EditProfile, name="editprofile"),

    # User Authentication
    path('sign-up/', views.RegisterView.as_view(), name="sign-up"),
    path('sign-in/', auth_views.LoginView.as_view(template_name="user/sign-in.html", redirect_authenticated_user=True), name='sign-in'),
    path('sign-out/', auth_views.LogoutView.as_view(template_name="user/sign-out.html"), name='sign-out'),
]