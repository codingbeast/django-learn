from django.shortcuts import render, redirect, HttpResponse
from django.views import View
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.urls import reverse
from .models import report_incident
from django.contrib.auth.models import User
# Create your views here.
class homepage(View):
    def get(self, request):
        return render(request, 'index.html')
class userlogin(View):
    def get(self, request):
        return render(request,"authentication-login1.html")
    def post(self, request):
        uname = request.POST.get('uname', None)
        password = request.POST.get('password', None)
        user = authenticate(username=uname, password=password)
        if user is not None:
            login(request, user)
            messages.info(request, f"You are now logged in as {uname}")
            next = request.GET.get("next","/")
            return redirect(next)
        else:
            messages.success(request, 'your login or password in Wrong')
            return redirect(reverse("main:userlogin"))
        #return HttpResponse(uname)
def userlogout(request):
    logout(request)
    return redirect(reverse("main:userlogin"))

@method_decorator(login_required(login_url='/login'), name='dispatch')
class report_form(View):
    def get(self, request):
        return render(request, "real_report_form.html")
    def post(self, request):
        incidentdepartment=request.POST.get("incidentdepartment")
        date = request.POST.get("date")
        time = request.POST.get("time")
        incidentlocation = request.POST.get("incidentlocation")
        initialseverity= request.POST.get("initialseverity")
        ImmediateActionTaken = request.POST.get("ImmediateActionTaken")
        SubIncident= request.POST.getlist("SubIncident")
        user = User.objects.get(id=request.user.id)
        obj = report_incident()
        obj.user = user
        obj.incidentdepartment = incidentdepartment
        obj.date = date
        obj.time = time
        obj.incidentlocation = incidentlocation
        obj.initialserverity = initialseverity
        obj.ImmediateAcitonTaken = ImmediateActionTaken
        obj.SubIncident = SubIncident
        obj.save()
        messages.success(request, 'Data is saved')
        return redirect(reverse("main:homepage"))