from rest_framework.decorators import api_view
from users.models import CustomUser, Song
from django.core.checks.messages import Error
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login
from django.contrib import messages
from users.forms import CustomUserCreationForm, SongCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.http import HttpResponse

# Create your views here.


class SignUpView(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/register.html'

def LogInView(request):
    if request.method != "POST":
        return HttpResponse("<script>alert(\"Method Unallowed\");window.location.replace(\"/\");</script>")
    else:
        email = request.POST.get('email', '')
        password = request.POST.get('password', '')
        user = authenticate(email=email, password=password)
        try:
            login(request, user)
        except NameError:
            messages.error(request, "Invalid Login Details")
            return HttpResponseRedirect('login/')

        if user != None:
            #if user.username != 'admin':
            return HttpResponse("<script>alert(\"Login Successfully\");window.location.replace(\"/\");</script>")
