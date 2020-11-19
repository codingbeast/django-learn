from django.shortcuts import render
from django.views import View
from django.shortcuts import render,HttpResponse
from django.contrib.auth import login, authenticate,logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect,reverse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm
# Create your views here.
def Register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        myform = SignUpForm(request.POST)
        if form.is_valid():
            user=form.save()
            user.refresh_from_db()
            user.student.num = form.cleaned_data.get('num')
            user.student.name = form.cleaned_data.get('name')
            user.student.surname = form.cleaned_data.get('surname')
            user.student.Age = form.cleaned_data.get('Age')
            user.student.Address = form.cleaned_data.get('Address')
            user.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            try:
                next = request.GET['next']
            except:
                next="/sec"
            return redirect(next)
        else:
            form = SignUpForm()
            return render(request, 'index.html', {'form': form,'myform': myform})
    else:
        #form = UserCreationForm()
        form = SignUpForm()
    return render(request, 'index.html', {'form': form})