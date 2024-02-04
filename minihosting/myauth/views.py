from django.contrib.auth.models import User
from django.http import HttpRequest
from django.shortcuts import render
from django.views.generic import DetailView
from django.urls import reverse_lazy


def profile(request: HttpRequest):
    return render(request, 'myauth/profile.html')





















# def login_view(request: HttpRequest) -> HttpResponse:
#     if request.method == "GET":
#         if request.user.is_authenticated:
#             return redirect('/admin/')
#
#         return render(request, "accounts/login.html")
#
#     username = request.POST["username"]
#     password = request.POST["password"]
#
#     user = authenticate(request, username=username, password=password)
#     if user is not None:
#         login(request, user)
#         return redirect('/admin/')
#     return render(request, "accounts/login.html", {"error": "Invalid login credentials"})
#
#
