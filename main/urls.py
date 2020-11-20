from django.urls import path, include
from .views import userlogin, homepage, userlogout,report_form
app_name = "main"
urlpatterns = [
    path('', homepage.as_view(), name="homepage"),
    path('login/', userlogin.as_view(),  name='userlogin'),
    path('logout/', userlogout, name='usrlogout'),
    path('report-form/', report_form.as_view(), name='report_form'),
]