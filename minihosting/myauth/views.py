from django.contrib.auth.models import User
from django.http import HttpRequest
from django.shortcuts import render
from django.views.generic import DetailView
from django.urls import reverse_lazy


def profile(self, request: HttpRequest):
    return render(request, 'myauth/profile.html')




















