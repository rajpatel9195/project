from django.shortcuts import render, redirect
from django.http import response, HttpResponse

# Create your views here.
from django.views import View
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

from django.contrib.auth.forms import UserCreationForm


class signup(View):
    def get(self, request, *args, **kwargs):
        form = UserCreationForm()
        return render(request, "signup.html", {"form": form})

    def post(self, request, *args, **kwargs):
        import pdb

        pdb.set_trace()
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            HttpResponse("saved")
        else:
            HttpResponse("hello")
