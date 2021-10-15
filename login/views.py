from django.shortcuts import render, redirect
from django.contrib.auth import logout


def account_logout(request):
    logout(request)
    return redirect('/')
