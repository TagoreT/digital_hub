from django.urls import path
from . import views

app_name = "authentication"

urlpatterns = [
    path("login/", views.login, name="login"),
    path("logout/", views.logout, name="logout"),
    # path("forget_password/",views.ForgetPassword,name="forgetpassword"),
	path("mentorRegistration/", views.mentorRegister, name="mentorRegister"),
	path("studentRegistration/", views.studentRegister, name="studentRegister"),
    path("reset_password/<token>/",views.ResetPassword,name="resetpassword"),
    path("changePassword/",views.changepassword,name="changepassword"),
    path("changingpwd/",views.changingpwd,name="changingpwd"),
]
